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

    def toDict(self):
        return {
                "unique_id": self.unique_id,
                # "mail": self.email,
                # "pseudo": self.pseudo,
                # "password": self.password,
            }

    def jwtGenerator(self):
        secret = os.environ.get('PRIVATE_KEY')
        public = os.environ.get('PUBLIC_KEY')
        if not public:
            return
        algo = os.environ.get('ALGO')
        if (secret == None):
            return Error
        JWT = jwt.encode(self.toDict() | {"time": peremptiontime().isoformat()}, secret, algorithm=algo)
        jwt.decode(JWT, public, algorithms=['RS256'])
        return JWT



