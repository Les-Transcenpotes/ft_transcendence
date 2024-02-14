from django.contrib.admin.views.autocomplete import JsonResponse
from .models import User
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def get_user(request):
    return JsonResponse({"user": "is"})


def new_client(request):
    name = request.GET.get('name')
    return JsonResponse({"actualClient": True})


def all_client(request):
    clients = [object.to_dict() for object in User.objects.all()]

    print(clients)
    return JsonResponse({"clients": list(clients)})





def add_friend(request):
    pass

def show_friends(request):
    pass

class newClientView(View):
    def post(self, request) -> JsonResponse :
        mailaddr = request.POST.get("mail")
        nickname = request.POST.get("nick")
        firstnme = request.POST.get("firstnme")
        lastname = request.POST.get("lastname")
        uniqueId = request.POST.get("id")

        if (not mailaddr or not nickname or not firstnme or not lastname or not uniqueId):
            return JsonResponse({"status": "Error", "Error": "field not filled"})
        newUser = User(uniqueId, firstnme, lastname, nickname, mailaddr)

        success = newUser.save()
        if success == False:
            return JsonResponse({"status": "Error"})
        return JsonResponse({"status" : "Success"})


    def get(self, request) -> JsonResponse :
        print("here")
        return JsonResponse({"status" : "getting client"})


# request friend
