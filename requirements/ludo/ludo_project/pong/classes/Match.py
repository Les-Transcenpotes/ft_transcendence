from pong.classes.GameSettings import gameSettings
from pong.classes.Ball import Ball

# A init autrement
class Match:
    def __init__(self):
        self.players = []
        self.score = [0, 0]
        self.ball = Ball(gameSettings=gameSettings())
        self.gameStarted = False
        self.startTime = 0
    
    def toDict(self):
        player1 = self.players[0]
        player2 = self.players[1]
        score1 = self.score[0]
        score2 = self.score[1]
        return ({
            'player1': player1,
            'player2': player2,
            'score1': score1,
            'score2': score2,
        })

matches = {}