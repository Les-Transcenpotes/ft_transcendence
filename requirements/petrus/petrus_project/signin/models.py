from django.db import models
from myjwt.jwt import JWT
from keys.privatekey import private_key

# Create your models here.


class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=15, unique=True)

    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.firstName = ""
        self.lastName = ""

    def toAlfred(self):
        return {
            "mail": self.email,
            "nick": self.pseudo,
            "id": self.unique_id,
            "firstnme": self.firstName,
            "lastname": self.lastName
        }

    def toDict(self):
        return {
            "unique_id": self.unique_id,
            "mail": self.email,
            "pseudo": self.pseudo,
            "password": self.password,
        }

    def __str__(self) -> str:
        return (f"""
                firstName : ${self.firstName}
                lastName : ${self.lastName}
                """)

    def toToken(self):
        return JWT.payloadToJwt(JWT.toPayload(self), private_key)

    @staticmethod
    def email_exists(email):
        return Client.objects.filter(email=email).exists()

    @staticmethod
    def nick_exists(nick):
        return Client.objects.filter(nick=nick).exists()
