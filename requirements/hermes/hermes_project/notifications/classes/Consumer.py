import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):

        # Join room group
        await self.channel_layer.group_add("matchmakingRoom", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("matchmakingRoom", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        state = text_data_json['state']
        
        # Send message to room group
        await self.channel_layer.group_send(
            "matchmakingRoom", {
                "type": state
            }
        )

    # Receive message from room group (mettre un _ dans le nom de la room entre les deux joueurs)
    async def Ready(self, event):
        pass
