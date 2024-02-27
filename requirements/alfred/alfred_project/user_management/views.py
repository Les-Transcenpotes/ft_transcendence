from django.contrib.admin.views.autocomplete import JsonResponse
from .models import User
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def all_client(request):
    clients = [object.to_dict() for object in User.objects.all()]
    return JsonResponse({"clients": list(clients)})


class createUserView(View):
    def post(self, request) -> JsonResponse:
        email = request.POST.get("mail")
        nickname = request.POST.get("nick")
        uniqueId = request.POST.get("id")

        print(email)
        print(nickname)
        print(uniqueId)

        if (email is None or not nickname is None or uniqueId is None):
            return JsonResponse(
                {"status": "Error", "Error": "field not filled"})

        newUser = User()
        newUser.unique_id = uniqueId
        newUser.unique_id = email
        newUser.nick = nickname

        success = newUser.save()
        if success == False:
            return JsonResponse({"status": "Error"})
        return JsonResponse({"status": "Success"})

    def get(self, request) -> JsonResponse:
        print("here")
        return JsonResponse({"status": "getting client"})
