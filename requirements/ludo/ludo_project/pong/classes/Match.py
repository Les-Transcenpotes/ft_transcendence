from requirements.ludo.ludo_project.pong.classes.GameSettings import gameSettings
from pong.classes.Ball import Ball

# A init autrement
class Match:
    def __init__(self):
        self.players = []
        self.score = [0, 0]
        self.ball = Ball(gameSettings=gameSettings())

matches = {}