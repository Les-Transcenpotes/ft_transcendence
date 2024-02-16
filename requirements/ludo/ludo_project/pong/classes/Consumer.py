from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("I am connected")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, gameData):
        gameDataJson = json.loads(gameData)
        ballPos = gameDataJson['ballPos']
        player1Pos = gameDataJson['player1Pos']
        player2Pos = gameDataJson['Player2Pos']

        await self.send(gameData=json.dumps({
            'ballPos': ballPos,
            'player1Pos': player1Pos,
            'player2Pos': player2Pos,
        }))