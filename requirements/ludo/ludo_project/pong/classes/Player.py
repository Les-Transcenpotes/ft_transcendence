# A recup via un requete au front !
from pong.gameLoop import match

class Player:
    def __init__(self, id):
        self.points = 0
        self.pos = match.screenHeight / 2
        self.up = False
        self.down = False
        self.id = id
        # speed = 0
        # acceleration = 0
    def move(self):
        mvt = self.down - self.up
        newPos = self.pos + mvt * match.screenHeight / 300
        if (newPos + match.playerHeight / 2 < match.screenHeight and newPos > match.playerHeight / 2):
            self.pos = newPos
