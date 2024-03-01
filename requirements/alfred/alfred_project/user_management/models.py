from django.contrib.admin.views.autocomplete import JsonResponse
from django.db import models


class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    nick = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    avatar = models.ImageField('avatars/', blank=True)
    friends = models.ManyToManyField('self', blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"""
                ${self.nick.__str__()}
                ${self.email.__str__()}
                ${self.unique_id.__str__()}
                """

    def to_dict(self):
        return {
            "unique_id": self.unique_id,
            "nick": self.nick,
            "email": self.email,
            "friends": self.list_friends(),
        }

    def friends_dict(self):
        return {
            "unique_id": self.unique_id,
            "nick": self.nick,
            "email": self.email,
            "avatar": "avatar"
        }

    def list_friends(self):
        return list([object.friends_dict() for object in self.friends.all()])


class FriendshipRequest(models.Model):
    sender = models.ForeignKey(
        Client,
        related_name="request_sended",
        on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        Client,
        related_name="request_receive",
        on_delete=models.CASCADE)
    objects = models.Manager

    def __str__(self):
        return f"""
                sender: ${self.sender.__str__()}
                receiver: ${self.receiver.__str__()}
                """

    def to_dict(self):
        return {
            "sender": self.sender.to_dict(),
            "receiver": self.receiver.to_dict(),
        }

    @staticmethod
    def processRequest(sender, receiver) -> JsonResponse:
        redondantRequest = FriendshipRequest.objects.filter(
            sender=sender, receiver=receiver).first()
        if redondantRequest is not None:
            print("damned")
            return JsonResponse({"Err": "redondantRequest"})

        pastRequest = FriendshipRequest.objects.filter(
            sender=receiver, receiver=sender)
        if pastRequest is None:
            newRequest = FriendshipRequest.objects.create(
                sender=sender, receiver=receiver)
            newRequest.save()
            return JsonResponse({"Friendship": "requested"})

        pastRequest.delete()
        sender.friends.add(receiver)
        # Hermes
        return JsonResponse({"Friendship": "established"})

    @staticmethod
    def deleteFriendship(emiter, target) -> JsonResponse:

        if target in emiter.friends.all():
            emiter.friends.remove(target)
            return JsonResponse({"Friendship": "deleted"})

        oldRequest = FriendshipRequest.objects.filter(
            sender=emiter, receiver=target)
        if oldRequest is not None:
            oldRequest.delete()
            return JsonResponse({"Friendship": "aborted"})

        oldRequest = FriendshipRequest.objects.filter(
            sender=target, receiver=emiter)
        if oldRequest is not None:
            oldRequest.delete()
            return JsonResponse({"Friendship": "aborted"})

        return JsonResponse({"Err": "Nothing to get deleted"})
