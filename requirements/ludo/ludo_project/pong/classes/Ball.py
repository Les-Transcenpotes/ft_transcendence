import math as m

# A recup via un requete au front !
screenWidth = 1080
screenLength = 1920

class Ball:
    def __init__(self):
        self.pos = [screenLength / 2, screenWidth / 2]
        self.speed = screenWidth / 5
        self.angle = 0
        self.size = screenWidth / 100
    def move(self):
        self.pos += [m.cos(self.angle), m.sin(self.angle)]
        assert(self.pos[0] > 0 & self.pos[0] < screenLength)
        assert(self.pos[1] > 0 & self.pos[1] < screenWidth)