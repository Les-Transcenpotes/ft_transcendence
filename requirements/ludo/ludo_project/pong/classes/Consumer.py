from channels.generic.websocket import AsyncWebsocketConsumer
from pong.classes.Match import match
from pong.classes.Player import Player
from pong.classes.gameSettings import gameSettings
from pong.classes.Ball import Ball
import json

# match[self.id] = moi
# match[(self.id + 1) % 2] = adversaire

class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        global match

        self.id = len(match.players)
        self.gameSettings = gameSettings(0, 0, 0, 0, 0)

        # Join room group
        await self.channel_layer.group_add("myRoom", self.channel_name)
        print("New consumer in room myRoom")

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        global match

        del match.players[self.id]
        await self.channel_layer.group_discard("myRoom", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        global match

        gameDataJson = json.loads(text_data)
        self.type = gameDataJson["type"]
        # Game logic here !

        # Send to room group
        if (self.type == "gameStart"):
            await self.channel_layer.group_send(
                "myRoom", {
                    "type": self.type,
                    "playerHeight": gameDataJson["playerHeight"],
                    "playerWidth": gameDataJson["playerWidth"],
                    "screenHeight": gameDataJson["screenHeight"],
                    "screenWidth": gameDataJson["screenWidth"],
                    "ballSize": gameDataJson["ballSize"],
                }
            )
        elif (self.type == "gameState"):
            await self.channel_layer.group_send(
                "myRoom", {
                    "type": "myState",
                    "id": self.id,
                    "meUp": gameDataJson["meUp"],
                    "meDown": gameDataJson["meDown"],
                }
            )

    async def gameStart(self, event):
        global match

        print("This is from the gameStart function")

        self.gameSettings = gameSettings(event["screenHeight"], event["screenWidth"], event["playerHeight"], event["playerWidth"], event["ballSize"]) #Changer les valeurs plutot aue de creer un nouvel objet ?
        match.players.append(Player(self.id, self.gameSettings))
        match.ball = Ball(self.gameSettings)

    # Receive gameState from room group
    async def myState(self, event):
        global match

        if (len(match.players) > 1):
            match.ball.move(match.players[0], match.players[1], self.gameSettings)

        if (event["id"] == self.id):
            match.players[self.id].up = event["meUp"]
            match.players[self.id].down = event["meDown"]
            match.players[self.id].move(self.gameSettings)
            # Send mePos to WebSocket
            if (self.id % 2 == 0):
                await self.send(text_data=json.dumps({
                    "type": "myState",
                    "mePos": match.players[self.id].pos,
                    "ballPosX": match.ball.pos[0],
                    "ballPosY": match.ball.pos[1],
                }))
            else:
                await self.send(text_data=json.dumps({
                    "type": "myState",
                    "mePos": match.players[self.id].pos,
                    "ballPosX": self.gameSettings.screenWidth - match.ball.pos[0],
                    "ballPosY": match.ball.pos[1], 
                }))

        else:
            match.players[(self.id + 1) % 2].up = event["meUp"]
            match.players[(self.id + 1) % 2].down = event["meDown"]
            match.players[(self.id + 1) % 2].move(self.gameSettings)
            # Send mePos to WebSocket
            if (self.id % 2 == 0):
                await self.send(text_data=json.dumps({
                    "type": "opponentState",
                    "opponentPos": match.players[(self.id + 1) % 2].pos,
                    "ballPosX": match.ball.pos[0],
                    "ballPosY": match.ball.pos[1],
                }))
            else:
                await self.send(text_data=json.dumps({
                    "type": "opponentState",
                    "opponentPos": match.players[(self.id + 1) % 2].pos,
                    "ballPosX": self.gameSettings.screenWidth - match.ball.pos[0],
                    "ballPosY": match.ball.pos[1],
                }))

