from django.db import Error, models
from django.utils.version import os
from jwt import encode
from signin.timeTool import peremptiontime

# Create your models here.

class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    pseudo = models.CharField(unique=True)

    def toDict(self):
        return {
                "unique_id": self.unique_id,
                "mail": self.email,
                "pseudo": self.pseudo,
                "password": self.password,
            }

    def jwtGenerator(self):
        secret = os.environ.get('SECRET')
        if (secret == None):
            return Error
        return encode(self.toDict() | {"time": peremptiontime()}, secret, algorithm="HS256")



