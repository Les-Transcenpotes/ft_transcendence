from django.contrib.admin.views.autocomplete import JsonResponse
from .models import User


def get_user():
    return JsonResponse({"oui": True})


def new_client(request):
    name = request.GET.get('name')
    return JsonResponse({"actualClient": True})


def all_client(request):
    clients = [object.to_dict() for object in User.objects.all()]
    print(clients)
    return JsonResponse({"clients": list(clients)})


