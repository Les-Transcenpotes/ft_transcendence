from django.http import HttpRequest, JsonResponse
from django.views import View
import requests

from signin.models import Client

# Create your views here.


def view_db(request: HttpRequest) -> JsonResponse:
    clients = [object.toDict() for object in Client.objects.all()]
    return JsonResponse({"clients": list(clients)})


class signinView(View):
    pass


class signupView(View):
    pass


class refreshTokenView(View):
    pass:


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
