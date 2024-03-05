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
        return JsonResponse({"Ava": Ava, "Id": id, "Nick": nick}, status=200)

    def post(self, request, string: str) -> JsonResponse:
        string = string
        id = request.POST.get("id")
        password = request.POST.get("pass")
        if id is None:
            return JsonResponse({"Err", "no id provided"})
        client = Client.objects.filter(unique_id=id).first()
        if client is None:
            return JsonResponse({"Err", "invalid id provided"})

        hashedPassword = make_password(password)
        if client.password != hashedPassword:
            return JsonResponse({"Err": "invalid password"})
        refresh_token = JWT.payloadToJwt(client.toDict(), JWT.privateKey)
        jwt = JWT.objectToAccessToken(client)
        return JsonResponse({"Ref": refresh_token, "Auth": jwt}, status=200)


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
                {"Err": "all information must be filled"}, status=200)
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
        request = requests.post(f'http://alfred/user/user-profile/{client.unique_id}',  # creation de la ressource
                                json=client.to_alfred())
        if request.status_code != 200:
            client.delete()
            return JsonResponse(request)

        # requests.post("http://mnemosine/",  # creation de la ressource dans la table,
        # json=client.to_mnemosine())

        # Alfred -> nickname email accessibility
        # Mnemosine -> id

        refresh_token = JWT.payloadToJwt(client.toDict(), JWT.privateKey)
        jwt = JWT.objectToAccessToken(client)
        return JsonResponse({"ref": refresh_token, "Auth": jwt}, status=200)


class refreshView(View):
    def get(self, request):
        request = request
        return JsonResponse({"refreshView": "not coded"})
        refresh_token = JWT.payloadToJwt(client.toDict(), JWT.privateKey)
        jwt = JWT.objectToAccessToken(client)
        if False:
            return JsonResponse({"Err": "Invalid refresh token"})
        return JsonResponse("")


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

        return JsonResponse({"status": "success"})
        return JsonResponse({"": ""})

def new_view(request, nick: str, mail: str, password: str):
    client = Client.objects.all().filter(nick=nick).first()
    # if yo is not None:
        # yo.delete()
        # return JsonResponse({"damned": "youpi"})

    print(mail, nick)
    # client = Client.objects.create(email=mail, password=make_password(password), nick=nick)
    # client.save()
    print(client.to_alfred())
    print(f'http://alfred:8001/user/user-profile/{client.unique_id}')
    request = requests.post(f'http://alfred:8001/user/user-profile/{client.unique_id}',  # creation de la ressource
                            json=client.to_alfred())
    print(request)
    return JsonResponse({"": ""}, safe=False)
