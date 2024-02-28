from channels.generic.websocket import AsyncWebsocketConsumer
from pong.classes.Match import match
from pong.classes.Player import Player
import json

# Commencer a reflechir a comment faire avec 2 joueurs separes !
# match[self.id] = moi
# match[(self.id + 1) % 2] = adversaire

# Cf doc django channels (Tuto part 2 and 3)
class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        global match

        self.id = len(match.players)
        match.players.append(Player(self.id))

        # Join room group
        await self.channel_layer.group_add("myRoom", self.channel_name)
        print("New consumer in room myRoom")

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
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
                    "screenHeight": gameDataJson["screenHeight"],
                    "screenWidth": gameDataJson["screenWidth"],
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
        match.playerHeight = event["playerHeight"]
        match.screenHeight = event["screenHeight"]
        match.screenWidth = event["screenWidth"]

        # if (self.id == 0):
        #     asyncio.create_task(gameLoop()) # Can't do this here, or only the host

    # Receive gameState from room group
    async def myState(self, event):
        global match

        if (event["id"] == self.id):
            match.players[self.id].up = event["meUp"]
            match.players[self.id].down = event["meDown"]
            match.players[self.id].move()
            # Send mePos to WebSocket
            await self.send(text_data=json.dumps({
                "type": "myState",
                "mePos": match.players[self.id].pos,
            }))

        else:
            match.players[(self.id + 1) % 2].up = event["meUp"]
            match.players[(self.id + 1) % 2].down = event["meDown"]
            match.players[(self.id + 1) % 2].move()
            # Send mePos to WebSocket
            await self.send(text_data=json.dumps({
                "type": "opponentState",
                "opponentPos": match.players[(self.id + 1) % 2].pos,
            }))

