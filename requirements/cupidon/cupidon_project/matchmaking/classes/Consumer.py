import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import redirect
from django.http import HttpResponse

playerList = []

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        global playerList
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add("matchmaking_room", self.channel_name)

        playerList.append("Player") # Get player name with the token here
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        global playerList
        await self.channel_layer.group_discard("matchmaking_room", self.channel_name)
        print("Bye !")
        playerList.remove("Player")

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        state = text_data_json["state"]
        
        # Send message to room group
        await self.channel_layer.group_send(
            "matchmaking_room", {"type": state}
        )

    # Receive message from room group
    async def Ready(self, event):
        if len(playerList) > 1:
            print("yo !")
            playerList.remove("Player")
            playerList.remove("Player")
            await self.send(json.dumps({"action": "redirect", "url": "https://localhost:8000/ludo/pong/"}))
    
    async def Leaving(self, event):
        global playerList
        print("Bye !")
        playerList.remove("Player")

