# A recup via un requete au front !
screenWidth = 1080
screenLength = 1920

class Player:
    width = screenWidth / 10
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.pos = screenWidth / 2
        # speed = 0
        # acceleration = 0
    def move(self, mvt):
        self.pos += mvt * screenWidth / 100
        assert(self.pos + self.width/2 < screenWidth)
        assert(self.pos - self.width/2 > 0)