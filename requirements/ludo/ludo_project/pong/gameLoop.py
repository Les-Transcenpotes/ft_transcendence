from pong.classes.Match import Match
import math as m
import time

screenWidth = 1920
screenHeight = 800 # Ne change que le rebond de la balle
diamater = 25
height = 180
width = 20

match = Match()

def isPlayerCollision(ball, player):
    if (ball.pos[1] > player.pos - height / 2 and
        ball.pos[1] < player.pos + height / 2):
        return True
    return False

def playerCollision(ball, player):
    impactToMid = (ball.pos[1] - player.pos) / (height * 0.5) # > 0 quand la balle tape en DESSOUS du milieu
    if (player.id == 0):
        ball.angle = - (m.PI / 4) * impactToMid
    elif (player.id == 1):
        ball.angle = m.PI + (m.PI / 4) * impactToMid

async def mySleep(duration):
    time.sleep(duration)

async def gameLoop():
    global match
    # End of point
    await mySleep(0.005)
    while (match.players[0].points < 3 or match.players[1].points < 3):

        # print(match.players[0].up)
        # print(match.players[0].id)
        # print(match.players[1].id)
        
        if (match.ball.pos[0] > screenWidth):
            match.players[0].points += 1
            match.ball.init()
        elif (match.ball.pos[0] < 0):
            match.players[1].points += 1
            match.ball.init()

        # Update positions
        match.ball.move()
        match.players[0].move()
        # match.players[1].move(match.players[1])

        # Collision with match.players[1]
        if (match.ball.pos[0] >= screenWidth - diamater + width and isPlayerCollision(match.ball, match.players[1])): 
            playerCollision(match.ball, match.players[1])
        

        # Collision with match.players[0]
        if (match.ball.pos[0] <= diamater + width and isPlayerCollision(match.ball, match.players[0])):
            playerCollision(match.ball, match.players[0])
        

        # Collision with walls
        if (match.ball.pos[1] <= diamater / 2 or match.ball.pos[1] >= screenHeight - diamater / 2):
            match.ball.angle = - match.ball.angle
