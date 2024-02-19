from channels.generic.websocket import AsyncWebsocketConsumer
import json

# Cf doc django channels (Tuto part 2 and 3)
class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        await self.channel_layer.group_add("self.room_group_name", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard("self.room_group_name", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        player1Pos = text_data_json["player1Pos"]

        # Send player1Pos to room group
        await self.channel_layer.group_send(
            "self.room_group_name", {"type": "chat_player1Pos", "player1Pos": player1Pos}
        )

    # Receive player1Pos from room group
    async def chat_player1Pos(self, event):
        player1Pos = event["player1Pos"]

        # Send player1Pos to WebSocket
        await self.send(text_data=json.dumps({"player1Pos": player1Pos}))