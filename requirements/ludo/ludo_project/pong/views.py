from django.shortcuts import render
from pong.classes import *

# Create your views here.

from django.http import HttpResponse

# Logic here

#A changer avec les websockets
def up_key():
    return True

#A changer avec les websockets
def down_key():
    return True    

def pong(request): # What's "request" ?
    return render(request, 'pong/test.html', {})

def result(request):
    return HttpResponse("You win or you lost, idk yet !")