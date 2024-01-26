from django.db import models

# player1 and player2 need to be unique identifier
class Match(models.Model):
    player1 = models.CharField()
    player2 = models.CharField()
    result = {player1: 0, player2: 0}

class Tournament(models.Model):
    matches = models.ManyToManyField(Match)

