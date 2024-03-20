from django.db import models

# Create your models here.


class Player(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    elo = models.IntegerField()
    games_played = models.ManyToManyField(
        'self',
        through='Game',
        related_name='players',
        symmetrical=False)
    tournaments_played = models.ManyToManyField(
        'Tournament', through='TournamentPlayer')

    objects = models.Manager()

    def to_dict(self):
        return {
            "Id": self.unique_id,
            "Elo": self.elo,
        }


class Game(models.Model):
    unique_id = models.BigAutoField(primary_key=True)
    player1 = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='games_as_player1')
    score1 = models.IntegerField()
    player2 = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='games_as_player2')
    score2 = models.IntegerField()


class Tournament(models.Model):
    name = models.CharField(max_length=255, unique=True)
    games = models.ManyToManyField(Game, through='TournamentGame')


class TournamentPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'tournament')


class TournamentGame(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tournament', 'game')
