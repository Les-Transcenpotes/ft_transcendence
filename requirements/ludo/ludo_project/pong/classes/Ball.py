import math as m

# A recup via un requete au front !
screenWidth = 1080
screenLength = 1920

class Ball:
    def __init__(self):
        self.pos = [screenLength / 2, screenWidth / 2]
        self.speed = screenWidth / 5
        self.angle = m.pi
        self.size = screenWidth / 100
    def move(self):
        self.pos += [m.cos(self.angle), m.sin(self.angle)]
    def init(self):
        self.pos = [screenLength / 2, screenWidth / 2]
        self.speed = screenWidth / 5
        self.angle = m.pi
        self.size = screenWidth / 100