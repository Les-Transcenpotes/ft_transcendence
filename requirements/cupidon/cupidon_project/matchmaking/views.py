from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from matchmaking.classes.Matchmaking import matchmaking

def matchmaking(request):
    return render(request, 'matchmaking/waitingRoom.html')