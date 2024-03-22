import json
from channels.generic.websocket import AsyncWebsocketConsumer
from tournament.classes.Tournament import tournaments

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        global tournaments

        # Join room group
        self.tournamentName = self.scope["url_route"]["kwargs"]["tournamentName"]
        self.myTournament = tournaments[self.tournamentName]
        self.id = len(self.myTournament.players) # We want it to be his place in the players array
        self.myName = len(self.myTournament.players) # I will need the id of the player.
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
        type = text_data_json['type']
        
        # Send message to room group
        await self.channel_layer.group_send(
            "tournamentsRoom", {
                "type": type
            }
        )

    async def Start(self, event):
        global tournaments
        
        self.myTournament.state += 1
        await self.send(json.dumps({
                "action": "redirect",
                }))
        
    async def StartRound(self, event):
        global tournaments

        await self.send(json.dumps({
                "action": "startMatch",
                "player1": self.myTournament.players[self.id - self.id % 2],
                "player2": self.myTournament.players[self.id + (1 - self.id % 2)],
                }))
        
    
        

