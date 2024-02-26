from django.db import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from shared.jwt import JWT
import requests

from signin.models import Client


def view_db(request: HttpRequest) -> JsonResponse:
    request = request
    clients = [object.toDict() for object in Client.objects.all()]
    return JsonResponse({"clients": list(clients)})


class signinView(View):
    """ se login """

    def get(self, request, string: str):

        request = request

        Ava: bool = True
        id: int = -1
        nick: str = "unknown"
        by_mail = Client.get_by_email(string)
        by_nick = Client.get_by_nick(string)

        if by_mail is not None:
            Ava = False
            id = by_mail.unique_id
            nick = by_mail.nick
        elif by_nick is not None:
            Ava = False
            id = by_nick.unique_id
            nick = by_nick.nick
        return JsonResponse({"Ava": Ava, "id": id, "nick": nick}, status=200)

    def post(self, request, string: str) -> JsonResponse:
        string = string
        id = request.POST.get("id")
        password = request.POST.get("pass")
        if id is None:
            return JsonResponse({"Err", "No id provided"})
        client = Client.objects.filter(unique_id=id).first()
        if client is None:
            return JsonResponse({"Err", "Invalid id provided"})

        hashedPassword = make_password(password)
        if client.password != hashedPassword:
            return JsonResponse({"Err": "Invalid password"})
        refresh_token = JWT.payloadToJwt(client.toDict(), JWT.privateKey)
        jwt = JWT.objectToAccessToken(client)
        return JsonResponse({"ref": refresh_token, "Auth": jwt}, status=200)


class signupView(View):
    """ s'inscrire """

    def get(self, request):
        request = request
        return JsonResponse({"Ava": True})

    def post(self, request):

        password = request.POST.get("pass")
        email = request.POST.get("mail")
        nick = request.POST.get("nick")
        accessibility = request.POST.get("accessibility")

        if not id or not password or not nick or not accessibility:
            return JsonResponse(
                {"Err": "All information must be filled"}, status=200)
        hashed_password = make_password(accessibility)

        client = Client()
        client.password = password
        client.email = email
        client.nick = nick

        try:
            client.save()
        except IntegrityError as e:
            print("An integrity error occured:", e)
            return JsonResponse({"Err": e}, status=409)

        # Alfred -> nickname email accessibility
        # Mnemosine -> id

        refresh_token = JWT.payloadToJwt(client.toDict(), JWT.privateKey)
        jwt = JWT.objectToAccessToken(client)

        return JsonResponse({"ref": refresh_token, "Auth": jwt}, status=200)


class refreshView(View):
    def get(self, request):
        request = request
        pass


"""
old views
"""


class checkInView(View):
    def get(self, request: HttpRequest, type: str, data: str) -> JsonResponse:
        if (type == "mail"):
            query = Client.objects.filter(email=data).first()
        else:
            query = Client.objects.filter(pseudo=data).first()
        if not query:
            return JsonResponse({"availability": True})
        return JsonResponse({"availability": False, "client": query.toDict()})

    def post(self, request: HttpRequest, checked: str,
             mail: str) -> JsonResponse:
        mailaddr = request.POST.get("mail")
        nickname = request.POST.get("nick")
        password = request.POST.get("pass")
        firstnme = request.POST.get("firstnme")
        lastname = request.POST.get("lastname")

        if (not mailaddr or not nickname or not password or not firstnme or not lastname):
            return JsonResponse(
                {"status": "Error", "msg": "All information must be filled"})

        newClient = Client(email=mailaddr,
                           pseudo=nickname,
                           password=password,
                           firstName=firstnme,
                           lastName=lastname)
        success = newClient.save()

        if success == False:
            return JsonResponse({"Error": "Intern database error"})

        response = requests.post("http://alfred:8000/user-managment/new-client/",
                                 json=newClient.toAlfred())
        return JsonResponse({"status": "success"})
        return JsonResponse({"": ""})


def bad(request: HttpRequest):
    print(request)
    return JsonResponse({"va te faire": "connard"}, status=400)
