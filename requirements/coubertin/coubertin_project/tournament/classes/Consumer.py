import json
from channels.generic.websocket import AsyncWebsocketConsumer
from tournament.classes.Tournament import tournaments

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        global tournaments

        # Join room group
        self.tournamentName = self.scope["url_route"]["kwargs"]["tournamentName"]
        print ("Tournament room name is " + self.tournamentName)

        await self.channel_layer.group_add("tournamentsRoom", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        global tournaments
        await self.channel_layer.group_discard("tournamentsRoom", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        state = text_data_json['state']
        
        # Send message to room group
        await self.channel_layer.group_send(
            "tournamentsRoom", {
                "type": state
            }
        )

    async def Ready(self, event):
        await self.send(json.dumps({
                "action": "redirect",
                }))
