import math as m
import time

# La balle est dans le repere de l'hote
class Ball:

    def __init__(self, gameSettings):
        self.pos = [gameSettings.screenWidth / 2, gameSettings.screenHeight / 2]
        self.speed = gameSettings.screenWidth / 5000
        self.angle = m.pi
        self.size = gameSettings.ballSize

    def newPoint(self, gameSettings):
        self.pos = [gameSettings.screenWidth / 2, gameSettings.screenHeight / 2]
        self.speed = gameSettings.screenWidth / 5000
        self.angle = m.pi
        self.size = gameSettings.ballSize

    def isPlayerCollision(self, player): # Identifier les joueurs par id (si pair, ils sont hotes sinon clients)
        if (self.pos[1] > player.pos - (player.height / 2) and
            self.pos[1] < player.pos + (player.height / 2)):
            return True
        return False

    def hostCollision(self, host):
        if (self.pos[0] <= self.size + host.width and self.isPlayerCollision(host)):
            impactToMid = ((self.pos[1] - host.pos) / (host.height * 0.5))
            self.angle = (m.pi / 4) * impactToMid
            self.speed *= 1.1

    def clientCollision(self, client, gameSettings):
        if (self.pos[0] >= gameSettings.screenWidth - (self.size + client.width) and self.isPlayerCollision(client)):
            impactToMid = ((self.pos[1] - client.pos) / (client.height * 0.5))
            self.angle = - (m.pi + (m.pi / 4) * impactToMid)
            self.speed *= 1.1
    
    def wallCollision(self, gameSettings):
        if (self.pos[1] <= self.size / 2 or self.pos[1] >= gameSettings.screenHeight - self.size / 2):
            self.angle = - self.angle

    def updatePoints(self, gameSettings):
        if (self.pos[0] < 0):
            self.newPoint(gameSettings)
            return 0
        elif (self.pos[0] > gameSettings.screenWidth):
            self.newPoint(gameSettings)
            return 1
        return -1

    def move(self, host, client, gameSettings):
        self.hostCollision(host)
        self.clientCollision(client, gameSettings)
        self.wallCollision(gameSettings)
        self.pos[0] += m.cos(self.angle) * self.speed
        self.pos[1] += m.sin(self.angle) * self.speed
        return (self.updatePoints(gameSettings))
        