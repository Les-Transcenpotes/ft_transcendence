from django.contrib.admin.views.autocomplete import JsonResponse
from django.utils.translation.trans_real import receiver
from user_management.models import Client, FriendshipRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


from shared.common_classes import User


class createUserView(View):
    def post(self, request) -> JsonResponse:
        # secu venant de petrus
        email = request.POST.get("mail")
        nickname = request.POST.get("nick")
        uniqueId = request.POST.get("id")

        if (email is None or not nickname is None or uniqueId is None):
            return JsonResponse(
                {"status": "Error", "Error": "field not filled"})

        newUser = Client()
        newUser.unique_id = uniqueId
        newUser.unique_id = email
        newUser.nick = nickname

        success = newUser.save()
        if success == False:
            return JsonResponse({"status": "Error"})
        return JsonResponse({"status": "Success"})

    def delete(self, request) -> JsonResponse:
        # secu venant de petrus
        return JsonResponse({})

    def patch(self, request):
        request = request


class personalInfoView(View):
    def get(self, request) -> JsonResponse:
        if request.user.is_autenticated is False:
            return JsonResponse({"Err": request.user.error})
        user = Client.objects.filter(unique_id=request.user.id).first()
        if user is None:
            return JsonResponse({"Err": "Internal Servor Error"}, status=500)
        return JsonResponse({"Information": user.to_dict()})

    def post(self, request) -> JsonResponse:
        if request.user.is_autenticated is False:
            return JsonResponse({"Err": request.user.error})
        user = Client.objects.filter(unique_id=request.user.id).first()
        if user is None:
            return JsonResponse({"Err": "Internal Servor Error"}, status=500)

        email = request.POST.get("mail")
        if email is not None:
            user.email = email
        nickname = request.POST.get("nick")
        if nickname is not None:
            user.nick = nickname

        # alfred -> notifier le changement

        user.update()
        return JsonResponse({"Information": user.to_dict()})


class clientInfoIdView(View):
    def get(self, request) -> JsonResponse:
        request = request
        nick = "nick"
        email = "mail"
        avatar = "avatar"
        return JsonResponse({"nick": nick, "mail": email, "avatar": avatar})


class friendView(View):
    def get(self, request, id: int) -> JsonResponse:
        emiter = Client.objects.get(unique_id=request.user.id)
        return JsonResponse({
            "id": request.user.id,
            "friends": [
                object.friends_dict()
                for object
                in emiter
                .friends
                .all()
            ],
            "requests": [
                {"id": object.sender.unique_id,
                 "nick": object.sender.nick}
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
            return JsonResponse({"Err": "Invalid id"})
        return FriendshipRequest.processRequest(receiver, sender)

    def delete(self, request, id: int) -> JsonResponse:
        emiter = Client.objects.get(unique_id=request.user.id)
        try:
            target = Client.objects.get(unique_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"Err": "Invalid id"})
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
