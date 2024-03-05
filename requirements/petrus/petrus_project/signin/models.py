from django.db import models


class Client(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    nick = models.CharField(max_length=16, unique=True)

    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def to_alfred(self):
        return {
            "mail": self.email,
            "nick": self.nick,
            "id": self.unique_id,
        }

    def to_mnemosine(self):
        return {
                "id": self.unique_id
        }

    def toDict(self):
        return {
            "id": self.unique_id,
            "mail": self.email,
            "nick": self.nick,
        }

    def __str__(self) -> str:
        return (f"""
                firstName : ${self.email}
                lastName : ${self.nick}
                """)

    @staticmethod
    def get_by_email(email):
        return Client.objects.filter(email=email).first()

    @staticmethod
    def get_by_nick(nick):
        return Client.objects.filter(nick=nick).first()
