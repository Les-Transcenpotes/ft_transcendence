from channels.generic.websocket import AsyncWebsocketConsumer
from pong.gameLoop import gameLoop, match
from pong.classes.Player import Player
import json
import asyncio

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
        await self.channel_layer.group_add("self.room_group_name", self.channel_name)
        print("New consumer in room self.room_group_name")

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("self.room_group_name", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        global match

        gameDataJson = json.loads(text_data)
        self.type = gameDataJson["type"]
        # Game logic here !

        # Send mePos to room group
        if (self.type == "gameStart"):
            await self.channel_layer.group_send(
                "self.room_group_name", {
                    "type": self.type,
                    "playerHeight": gameDataJson["playerHeight"],
                    "screenHeight": gameDataJson["screenHeight"],
                    "screenWidth": gameDataJson["screenWidth"],
                }
            )
        else:
            await self.channel_layer.group_send(
                "self.room_group_name", {
                    "type": self.type,
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
    async def gameState(self, event):
        global match

        match.players[self.id].up = event["meUp"]
        match.players[self.id].down = event["meDown"]
        match.players[self.id].move()
        # Send mePos to WebSocket
        await self.send(text_data=json.dumps({
            "mePos": match.players[self.id].pos,
            # "advPos": match.players[(self.id + 1) % 2].pos,
        }))