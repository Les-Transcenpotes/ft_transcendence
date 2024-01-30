from django.contrib.admin.views.autocomplete import JsonResponse
from .models import User, YourModelForm
from django.shortcuts import render


def get_user():
    return JsonResponse({"oui": True})


def new_client(request):
    name = request.GET.get('name')
    return JsonResponse({"actualClient": True})


def all_client(request):
    clients = [object.to_dict() for object in User.objects.all()]

    print(clients)
    return JsonResponse({"clients": list(clients)})


def create_view(request):
    if request.method == 'GET':
        return render(request, 'template_name.html', {'form':YourModelForm()})

    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return JsonResponse({'success': True})


def add_friend(request):
    pass

def show_friends(request):
    pass



# request friend
