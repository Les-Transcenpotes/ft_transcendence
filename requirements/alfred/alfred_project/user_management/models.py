from django.db import models

# Create your models here.
# Need to instantiate objects for

class User(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=20)
    nick = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    # avatar = models.ImageField('avatars/')
    friends = models.ManyToManyField('self', blank=True)
    objects = models.Manager();

    def __init__(self, unique_id, firstName, lastName, nick, email):
        self.unique_id = unique_id
        self.firstName = firstName
        self.lastName = lastName
        self.nick = nick
        self.email = email

    def __str__(self):
        return self.firstName.__str__()


    def to_dict(self):
        return {
                "unique_id" : self.unique_id,
                "firstName" : self.firstName,
                "lastName" : self.lastName,
                "nick" : self.nick,
                "email" : self.email,
        }
