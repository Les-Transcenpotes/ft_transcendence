from django.db import models
from myjwt.jwt import JWT
from keys.privatekey import private_key

# Create your models here.

class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=15, unique=True)

    objects = models.Manager();

    def __init__(self, email, pseudo, password, firstName, lastName, ):
        self.lastName = lastName
        self.firstName = firstName
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

    def __str__(self) -> str:
        return ("firstName : "
            + self.firstName
            + "\nlastName : "
            + self.lastName
            + "\n"
        )

    def newAccessToken(self):
        JWT.payloadToJwt(JWT.toPayload(self), private_key)

