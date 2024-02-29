from .Ball import Ball
from .gameSettings import gameSettings

# A iniit autrement
class Match:
    def __init__(self):
        self.players = []
        self.ball = Ball(gameSettings=gameSettings(0, 0, 0, 0))

match = Match()