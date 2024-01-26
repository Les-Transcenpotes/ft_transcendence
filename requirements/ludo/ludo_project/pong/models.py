from django.db import models
import math as m

# Create your models here.

screenWidth = 1080
screenLength = 1920

class Player:
    def __init__(self, name):
        self.name = name
        points = 0
        pos = screenWidth / 2
        # speed = 0
        # acceleration = 0
        width = screenWidth / 10
    def move(self, mvt):
        self.pos += mvt * screenWidth / 100
        assert(self.pos + self.width/2 < screenWidth)
        assert(self.pos - self.width/2 > 0)

class Ball:
    def __init__(self):
        pos = [screenLength / 2, screenWidth / 2]
        speed = screenWidth / 5
        angle = 0
        size = screenWidth / 100
    def move(self):
        self.pos += [m.cos(self.angle), m.sin(self.angle)]
        assert(self.pos[0] > 0 & self.pos[0] < screenLength)
        assert(self.pos[1] > 0 & self.pos[1] < screenWidth)
