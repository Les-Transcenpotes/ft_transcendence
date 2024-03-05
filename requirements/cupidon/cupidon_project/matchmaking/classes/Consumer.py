import json
from channels.generic.websocket import AsyncWebsocketConsumer
from matchmaking.classes.Matchmaking import matchmaking

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        global matchmaking

        # Join room group
        await self.channel_layer.group_add("matchmakingRoom", self.channel_name)

        self.id = len(matchmaking.waitingList)
        matchmaking.waitingList.append(self.id) # Get player name with the token here
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        global matchmaking
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
        if len(matchmaking.waitingList) > 1:
            matchmaking.inGame[str(matchmaking.waitingList[0]) + '-' + str(matchmaking.waitingList[1])] = [str(matchmaking.waitingList[0]), str(matchmaking.waitingList[1])]
            # matchmaking.waitingList.remove[matchmaking.waitingList[0]]
            # matchmaking.waitingList.remove[matchmaking.waitingList[1]]
            await self.send(json.dumps({
                    "action": "redirect", 
                    "url": "https://localhost:8000/ludo/pong/"
                            + str(matchmaking.waitingList[0])
                            + "-"
                            + str(matchmaking.waitingList[1])
                            + "/"
                    }))
