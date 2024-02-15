from django.http import HttpRequest, JsonResponse
from django.views import View
import requests

from signin.models import Client
from myjwt.decorator import exempt_JWT

# Create your views here.

class SigninView(View):
    def get(self, request) -> JsonResponse :
        mailaddr = "bon@gmail.com"
        nickname = "yo"
        password = "yo"
        firstnme = "yo"
        lastname = "yo"

        newClient = Client(email=mailaddr,
                           pseudo=nickname,
                           password=password,
                           firstName=firstnme,
                           lastName=lastname)

        success = newClient.save()

        response = requests.post("http://alfred:8000/user-managment/new-client/",
                                 data=newClient.toAlfred())
        if (response.status_code == 200):
            print(response.json)
            return (JsonResponse(response.json()))
        return JsonResponse({"is": "error"})

    def post(self, request) -> JsonResponse :
        mailaddr = request.POST.get("mail")
        nickname = request.POST.get("nick")
        password = request.POST.get("pass")
        firstnme = request.POST.get("firstnme")
        lastname = request.POST.get("lastname")

        if (not mailaddr or not nickname or not password or not firstnme or not lastname):
            return JsonResponse({"status": "Error", "msg": "All information must be filled"})

        newClient = Client(email=mailaddr,
                           pseudo=nickname,
                           password=password,
                           firstName=firstnme,
                           lastName=lastname)
        success = newClient.save()
        print("this is the id")
        print(newClient.unique_id)

        if success == False:
            return JsonResponse({"status": "Error", "msg": "Intern database error"})

        response = requests.post("http://alfred:8000/user-managment/new-client/",
                                 json=newClient.toAlfred())

        return JsonResponse({"status" : "success"})

@exempt_JWT
def first_connection(request: HttpRequest):
    if request.method:
        return JsonResponse({"is": "good"})

