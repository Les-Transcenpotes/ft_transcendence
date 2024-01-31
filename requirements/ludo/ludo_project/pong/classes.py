
import math as m
from channels.generic.websocket import AsyncWebsocketConsumer
import json


screenWidth = 1080
screenLength = 1920


class PongGameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

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