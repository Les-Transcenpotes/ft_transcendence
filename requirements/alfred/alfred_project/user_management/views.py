from django.contrib.admin.views.autocomplete import JsonResponse
from user_management.models import Client, FriendshipRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json


class userInfoView(View):
    def get(self, request, id: int) -> JsonResponse:
        client = Client.objects.get(unique_id=id)
        if id == 0 or id == request.user.id:
            return JsonResponse(client.personal_dict())
        try:
            target = Client.objects.get(unique_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"Err", "invalid id"})
        if client in target.friends.all():
            return JsonResponse({target.friends_dict()})
        return JsonResponse(client.public_info_dict())

    def patch(self, request, id: int) -> JsonResponse:
        client = Client.objects.get(request.user.id)
        marker: bool = False
        try:
            data = json.loads(request.body)
        except BaseException:
            return JsonResponse({"Err": "JSON cannot be extracted"})
        if "Avatar" in data:
            marker = True
            client.avatar = client["avatar"]
            # suppression de l'ancien avatar
        if "Accessibility" in data:
            marker = True
            # client accessibility update
        if marker is False:
            return JsonResponse({"Err": "no changes"})
        client.update()
        return JsonResponse({"Client": "updated"})


class userProfileView(View):
    def post(self, request, id: int) -> JsonResponse:
        email = request.POST.get("mail")
        nickname = request.POST.get("nick")
        unique_id = id
        if (email is None or not nickname is None or unique_id is None):
            return JsonResponse({"Err": "field not filled"})
        newUser = Client.objects.create(
            unique_id=unique_id,
            email=email,
            nick=nickname
        )
        try:
            newUser.save()
        except BaseException:
            return JsonResponse({"Err": "internal server error"})
        return JsonResponse({"Client": "created"})

    def patch(self, request, id: int) -> JsonResponse:
        try:
            client = Client.objects.get(unique_id=id)
        except BaseException:
            return JsonResponse({"Err": "invalid id"})
        marker: bool = False
        try:
            data = json.loads(request.body)
        except BaseException:
            return JsonResponse({"Err": "JSON cannot be extracted"})
        if "Nick" in data:
            marker = True
            client.nick = client["nick"]
        if "Email" in data:
            marker = True
            client.email = client["email"]
        if marker is False:
            return JsonResponse({"Err": "no changes"})
        client.update()
        return JsonResponse({"Client": "updated"})

    def delete(self, request, id: int) -> JsonResponse:
        try:
            client = Client.objects.get(unique_id=id)
        except BaseException:
            return JsonResponse({"Err": "invalid id"})
        try:
            client.delete()
        except BaseException:
            return JsonResponse({"Err": "internal database error"})
        return JsonResponse({"Client": "suppressed"})


class friendView(View):
    def get(self, request, id: int) -> JsonResponse:
        emiter = Client.objects.get(unique_id=request.user.id)
        return JsonResponse({
            "id": request.user.id,
            "friends": [
                {"id": object.unique_id,
                 "nick": object.nick,
                 "mail": object.email,
                 "avatar": object.avatar}
                for object
                in emiter
                .friends
                .all()
            ],
            "requests": [
                {"id": object.sender.unique_id,
                 "nick": object.sender.nick,
                 "avatar": object.sender.avatar}
                for object in list(
                    FriendshipRequest
                    .objects
                    .filter(receiver=emiter)
                )
            ],
        })

    def post(self, request, id: int) -> JsonResponse:
        sender = Client.objects.get(unique_id=request.user.id)
        try:
            receiver = Client.objects.get(unique_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"Err": "invalid id"})
        return FriendshipRequest.processRequest(receiver, sender)

    def delete(self, request, id: int) -> JsonResponse:
        emiter = Client.objects.get(unique_id=request.user.id)
        try:
            target = Client.objects.get(unique_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"Err": "invalid id"})
        return FriendshipRequest.deleteFriendship(emiter, target)


@csrf_exempt
def createUser(request):
    nick = "arthur"
    request = request
    mail = "delafforest@gmail.com"
    client = Client.objects.create(nick=nick, email=mail)
    client.save()
    return JsonResponse({nick: mail})


@csrf_exempt
def view_db(request):
    request = request
    clients = [object.to_dict() for object in Client.objects.all()]
    return JsonResponse({"clients": list(clients)})
