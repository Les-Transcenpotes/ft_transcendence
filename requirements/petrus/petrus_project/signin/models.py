from django.db import Error, models
from django.utils.version import os
import jwt
from signin.timeTool import peremptiontime

# Create your models here.

class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=15, unique=True)

    objects = models.Manager();

    def __init__(self, email, pseudo, password, nick, firstName, lastName, ):
        self.lastName = lastName
        self.firstName = firstName
        self.nick = nick
        self.password = password
        self.pseudo = pseudo
        self.email = email

    def toDict(self):
        return {
                "unique_id": self.unique_id,
                # "mail": self.email,
                # "pseudo": self.pseudo,
                # "password": self.password,
            }



