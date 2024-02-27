from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def matchmaking(request):
    return render(request, 'matchmaking/waitingRoom.html')