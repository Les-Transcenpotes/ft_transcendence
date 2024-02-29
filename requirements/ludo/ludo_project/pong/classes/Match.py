from pong.classes.gameSettings import gameSettings
from pong.classes.Ball import Ball

# A init autrement
class Match:
    def __init__(self):
        self.players = []
        self.score = {"host": 0, "client": 0}
        self.ball = Ball(gameSettings=gameSettings(0, 0, 0, 0, 0))

match = Match()