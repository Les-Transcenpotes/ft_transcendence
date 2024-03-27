import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):

        # Join room group
        await self.channel_layer.group_add("notificationRoom", self.channel_name)
        await self.accept()
        self.name = 'test'

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("notificationRoom", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        source = text_data_json['source']
        target = text_data_json['target']
        
        # Send message to room group
        await self.channel_layer.group_send(
            "notificationRoom", {
                "type": type,
                "target": target,
                "source": source,
            }
        )

    # Receive message from room group
    async def FriendRequest(self, event):
        if event['target'] == self.name:
            await self.send (text_data=json.dumps({
            "type": "friendRequest",
            "source": event['source'],
        }))

    async def GameInvite(self, event):
        if event['target'] == self.name:
            await self.send (text_data=json.dumps({
            "type": "gameInvite",
            "source": event['source'],
        }))

    async def TournamentInvite(self, event):
        if event['target'] == self.name:
            await self.send (text_data=json.dumps({
            "type": "tournamentInvite",
            "source": event['source'],
        }))

