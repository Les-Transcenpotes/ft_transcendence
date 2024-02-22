from .Ball import Ball

# A iniit autrement
class Match:
    def __init__(self):
        self.players = []
        self.ball = Ball()
        self.screenHeight = 400
        self.screenWidth = 1920
        self.playerHeight = 180