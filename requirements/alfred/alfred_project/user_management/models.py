from typing import Tuple
from django.db import models
from django import forms
from django.http import JsonResponse
from django.views import View

# Create your models here.
# Need to instantiate objects for

class User(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    pseudo = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    # avatar = models.ImageField('avatars/')
    friends = models.ManyToManyField('self', blank=True)


    objects = models.Manager();

    def saveUser(self):
        pass

    def __str__(self):
        return self.first_name.__str__()


    def to_dict(self):
        return {
                # 'avatar': self.avatar,
                'email': self.email,
                'pseudo': self.pseudo,
                'last_name': self.last_name,
                'id': self.unique_id,
                'name': self.first_name,
        }

class UserView(View):
    def post(self, request) -> JsonResponse :
        first_name = request.POST.get('first_name')
        pseudo = request.POST.get('pseudo')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        info = first_name, last_name, pseudo, email

        if not self.formIsComplete(info):
            return JsonResponse({"status": False})

        newUser = User.objects.create()

        return JsonResponse({"status": True})

    def get(self, request) -> JsonResponse :
        try:
            id = request.GET.get('unique_id')
            user = User.objects.get(unique_id=1)
            data = {
                    "status": True,
                    "user": {
                        'email': user.email,
                        'pseudo': user.pseudo,
                        'last_name': user.last_name,
                        'id': user.unique_id,
                        'name': user.first_name,
                }
            }
        except User.DoesNotExist:
            data = {
                "status": False,
                "message": "Id wasn't save in db"
            }
        return JsonResponse(data)

    def formIsComplete(self, info) -> Tuple[bool, str]:
        first_name, last_name, pseudo, email = info
        if not first_name or not last_name or not pseudo or not email:
            return False, "badForm"
        return True, "Success"


class YourModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'pseudo', 'email', ]

