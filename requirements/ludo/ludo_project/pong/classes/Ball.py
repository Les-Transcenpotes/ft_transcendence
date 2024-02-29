import math as m

# La balle est dans le repere de l'hote
class Ball:

    def __init__(self, gameSettings):
        self.pos = [gameSettings.screenWidth / 2, gameSettings.screenHeight / 2]
        self.speed = gameSettings.screenWidth / 5000
        self.angle = m.pi
        self.size = gameSettings.ballSize # A recup du front

    def start(self, gameSettings):
        self.pos = [gameSettings.screenWidth / 2, gameSettings.screenHeight / 2]
        self.speed = gameSettings.screenWidth / 5000
        self.angle = m.pi
        self.size = gameSettings.ballSize / 100

    def isPlayerCollision(self, player): # Identifier les joueurs par id (si pair, ils sont hotes sinon clients)
        if (self.pos[1] > player.pos - (player.height / 2) and
            self.pos[1] > player.pos - (player.height / 2)):
            return True
        return False

    def hostCollision(self, host):
        if (self.pos[0] <= self.size + host.width and self.isPlayerCollision(host)):
            impactToMid = ((self.pos[1] - host.pos) / (host.height * 0.5))
            self.angle = (m.pi / 4) * impactToMid

    def clientCollision(self, client, gameSettings):
        if (self.pos[0] >= gameSettings.screenWidth - self.size + client.width and self.isPlayerCollision(client)):
            impactToMid = ((self.pos[1] - client.pos) / (client.height * 0.5))
            self.angle = - (m.pi + (m.pi / 4) * impactToMid)
    
    def wallCollision(self, gameSettings):
        if (self.pos[1] <= self.size / 2 or self.pos[1] >= gameSettings.screenHeight - self.size / 2):
            self.angle = - self.angle

    def move(self, host, client, gameSettings):
        self.hostCollision(host)
        self.clientCollision(client, gameSettings)
        self.wallCollision(gameSettings)
        self.pos[0] += m.cos(self.angle) * self.speed
        self.pos[1] += m.sin(self.angle) * self.speed