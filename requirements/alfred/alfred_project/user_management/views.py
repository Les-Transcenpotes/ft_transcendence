from django.contrib.admin.views.autocomplete import JsonResponse
from .models import User
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def all_client(request):
    clients = [object.to_dict() for object in User.objects.all()]
    return JsonResponse({"clients": list(clients)})


class newClientView(View):
    def post(self, request) -> JsonResponse:
        mailaddr = request.POST.get("mail")
        nickname = request.POST.get("nick")
        firstnme = request.POST.get("firstnme")
        lastname = request.POST.get("lastname")
        uniqueId = request.POST.get("id")

        print(mailaddr)
        print(nickname)
        print(firstnme)
        print(lastname)
        print(uniqueId)

        if (not mailaddr or not nickname or not firstnme or not lastname or not uniqueId):
            return JsonResponse(
                {"status": "Error", "Error": "field not filled"})

        newUser = User(uniqueId, firstnme, lastname, nickname, mailaddr)

        success = newUser.save()
        if success == False:
            return JsonResponse({"status": "Error"})
        return JsonResponse({"status": "Success"})

    def get(self, request) -> JsonResponse:
        print("here")
        return JsonResponse({"status": "getting client"})
