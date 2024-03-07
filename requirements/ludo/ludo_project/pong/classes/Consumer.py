from channels.generic.websocket import AsyncWebsocketConsumer
from pong.classes.Match import matches, Match
from pong.classes.Player import Player
from pong.classes.gameSettings import gameSettings
from pong.classes.Ball import Ball
import json

# match[self.id] = moi
# match[(self.id + 1) % 2] = adversaire

class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        global matches

        self.roomName = self.scope["url_route"]["kwargs"]["roomName"]
        print("Room name is " + self.roomName)

        if (self.roomName not in matches):
            matches[self.roomName] = Match()

        # Join room group
        await self.channel_layer.group_add(self.roomName, self.channel_name)

        self.myMatch = matches[self.roomName]
        self.id = len(self.myMatch.players)
        self.gameSettings = gameSettings(0, 0, 0, 0, 0) # Voir si on peut faire autrement
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        global matches

        del self.myMatch.players[self.id]
        await self.channel_layer.group_discard(self.roomName, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        global matches

        gameDataJson = json.loads(text_data)
        self.type = gameDataJson["type"]
        # Game logic here !

        # Send to room group
        if (self.type == "gameStart"):
            await self.channel_layer.group_send(
                self.roomName, {
                    "type": self.type,
                    "playerHeight": gameDataJson["playerHeight"],
                    "playerWidth": gameDataJson["playerWidth"],
                    "screenHeight": gameDataJson["screenHeight"],
                    "screenWidth": gameDataJson["screenWidth"],
                    "ballSize": gameDataJson["ballSize"],
                }
            )

        elif (self.type == "gameState"):
            await self.channel_layer.group_send(
                self.roomName, {
                    "type": "myState",
                    "id": self.id,
                    "frames": gameDataJson["frames"],
                }
            )

    async def gameStart(self, event):
        global matches

        print("This is from the gameStart function")

        self.gameSettings = gameSettings(event["screenHeight"], event["screenWidth"], event["playerHeight"], event["playerWidth"], event["ballSize"]) #Changer les valeurs plutot aue de creer un nouvel objet ?
        self.myMatch.players.append(Player(self.id, self.gameSettings))
        self.myMatch.ball = Ball(self.gameSettings)

    async def updateScore(self, event):
        await self.send (text_data=json.dumps({
            "type": "updateScore",
            "myScore": self.myMatch.score[self.id],
            "opponentScore": self.myMatch.score[(self.id + 1) % 2],
        }))

    async def gameEnd(self, event):
        if (event["winner"] == self.id):
            await self.send (text_data=json.dumps({
                "type": "youWin",
                "myScore": self.myMatch.score[self.id],
                "opponentScore": self.myMatch.score[(self.id + 1) % 2],
            }))
        else:
            await self.send (text_data=json.dumps({
                "type": "youLose",
                "myScore": self.myMatch.score[self.id],
                "opponentScore": self.myMatch.score[(self.id + 1) % 2],
            }))
        # requests.post() # Poster direct a la db
            
    async def gameLogic(self, frames, id):
        global matches

        for frame in frames:
            self.myMatch.players[id].up = frames[frame]["meUp"]
            self.myMatch.players[id].down = frames[frame]["meDown"]
            self.myMatch.players[id].move(self.gameSettings)

            # Ball and score management
            if (len(self.myMatch.players) > 1):
                pointWinner = self.myMatch.ball.move(self.myMatch.players[0], self.myMatch.players[1], self.gameSettings)
                if (pointWinner != -1):
                    self.myMatch.score[pointWinner] += 1
                    await self.channel_layer.group_send (
                        self.roomName, {
                            "type": "updateScore",
                        }
                    )
                if (self.myMatch.score[self.id] == 5):
                    await self.channel_layer.group_send (
                        self.roomName, {
                            "type": "gameEnd",
                            "winner": self.id
                        }
                    )

    # Receive gameState from room group
    async def myState(self, event):
        global matches

        if (event["id"] == self.id):
            await self.gameLogic(event["frames"], self.id)
            if (self.id % 2 == 0):
                await self.send(text_data=json.dumps({
                    "type": "myState",
                    "mePos": self.myMatch.players[self.id].pos,
                    "ballPosX": self.myMatch.ball.pos[0],
                    "ballPosY": self.myMatch.ball.pos[1],
                }))
            else:
                await self.send(text_data=json.dumps({
                    "type": "myState",
                    "mePos": self.myMatch.players[self.id].pos,
                    "ballPosX": self.gameSettings.screenWidth - self.myMatch.ball.pos[0],
                    "ballPosY": self.myMatch.ball.pos[1],
            }))
                
        else:
            await self.gameLogic(event["frames"], (self.id + 1) % 2)
            if (self.id % 2 == 0):
                await self.send(text_data=json.dumps({
                    "type": "opponentState",
                    "opponentPos": self.myMatch.players[(self.id + 1) % 2].pos,
                    "ballPosX": self.myMatch.ball.pos[0],
                    "ballPosY": self.myMatch.ball.pos[1],
                }))
            else:
                await self.send(text_data=json.dumps({
                    "type": "opponentState",
                    "opponentPos": self.myMatch.players[(self.id + 1) % 2].pos,
                    "ballPosX": self.gameSettings.screenWidth - self.myMatch.ball.pos[0],
                    "ballPosY": self.myMatch.ball.pos[1],
                }))
