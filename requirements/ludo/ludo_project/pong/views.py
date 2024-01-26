from django.shortcuts import render
from pong.models import *
import time

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse # First arg of a Jsonresponse is a dictionnary

# Logic here

#A changer avec les websockets
def up_key():
    return True

#A changer avec les websockets
def down_key():
    return True    

def pong(request): # What's "request" ?
    player1 = Player("Brieuc")
    player2 = Player("Thea")
    while True:
        if up_key():
            player1.move(1)
            time.sleep(0.1)
            return HttpResponse("You pressed the up key!")
        if down_key():
            player1.move(1)
            time.sleep(0.1)
            return HttpResponse("You pressed the down key!")

def result(request):
    return HttpResponse("You win or you lost, idk yet !")