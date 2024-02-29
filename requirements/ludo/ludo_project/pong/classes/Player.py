class Player:
    def __init__(self, id, gameSettings):
        self.width = gameSettings.playerWidth
        self.height = gameSettings.playerHeight
        self.points = 0
        self.pos = gameSettings.screenHeight / 2
        self.up = False
        self.down = False
        self.id = id
        # speed = 0
        # acceleration = 0
    def move(self, gameSettings):
        mvt = self.down - self.up
        newPos = self.pos + mvt * gameSettings.screenHeight / 300
        if (newPos + gameSettings.playerHeight / 2 < gameSettings.screenHeight and newPos > gameSettings.playerHeight / 2):
            self.pos = newPos
