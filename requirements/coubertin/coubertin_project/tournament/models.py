from django.db import models
from django.contrib.auth.models import User

# name need to be a unique identifier
class Tournament(models.Model):
    name = models.CharField(max_length=50)
    maxPlayers = models.IntegerField()
    password = models.CharField(max_length=20)
    #start date ?

    def __str__(self):
        return self.name.__str__()
    
# important if we have several tournament modes
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Attention pas de primary key, pb ?
    tournament = models.ManyToManyField(Tournament)

    def __str__(self):
        return self.user.get_short_name()

# player1 and player2 need to be unique identifier
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE) # Pas sur de la cascade
    players = models.ManyToManyField(Player),
    winner = models.ForeignKey(Player, on_delete=models.CASCADE) # Pas sur de la cascade
    # player1 = models.ForeignKey(Player, on_delete=models.CASCADE) # Pas sur de la cascade
    # player2 = models.ForeignKey(Player, on_delete=models.CASCADE) # Pas sur de la cascade
   
