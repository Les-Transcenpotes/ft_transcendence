from django.db import models

# Create your models here.
# Need to instantiate objects for


class User(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    nick = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    # avatar = models.ImageField('avatars/')
    # friends = models.ManyToManyField('self', blank=True)
    objects = models.Manager()


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return f"""
                ${self.nick.__str__()}
                ${self.email.__str__()}
                ${self.unique_id.__str__()}
                """

    def to_dict(self):
        return {
            "unique_id": self.unique_id,
            "nick": self.nick,
            "email": self.email,
        }
