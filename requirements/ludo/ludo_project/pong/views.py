from django.shortcuts import render

# Create your views here.

def pong(request, roomName):
    return render(request, 'pong/pong.html', {"roomName": roomName})
