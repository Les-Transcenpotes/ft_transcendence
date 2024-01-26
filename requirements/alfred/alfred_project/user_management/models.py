from enum import unique
from django.db import models

# Create your models here.
# Need to instantiate objects for

class User(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    pseudo = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    avatar = models.ImageField('avatars/')
    objects = models.Manager();


    def __str__(self):
        return self.first_name.__str__()


    def to_dict(self):
        return {
                'avatar': self.avatar,
                'email': self.email,
                'pseudo': self.pseudo,
                'last_name': self.last_name,
                'id': self.unique_id,
                'name': self.first_name,
        }



