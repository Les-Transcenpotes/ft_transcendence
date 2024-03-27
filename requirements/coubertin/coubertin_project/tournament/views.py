from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tournament.classes.Tournament import Tournament, tournaments
import json
import io

class createTournament(View):
    def post(self, request):
        global tournaments

        data = json.load(io.BytesIO(request.body))
        tournamentName = data.get('tournamentName', None)
        nbPlayers = data.get('nbPlayers', None)
        tournaments[tournamentName] = Tournament(tournamentName, nbPlayers)

class joinTournament(View):
    def post(self, request):
        global tournaments

        data = json.load(io.BytesIO(request.body))
        tournamentName = data.get('tournamentName', None)
        if (tournamentName not in tournaments):
            return JsonResponse({'Err': 'tournament does not exists'})
        if (tournaments[tournamentName].nbPlayers == len(tournaments[tournamentName].players)):
            return JsonResponse({'Err': 'tournament is already full'})
        tournaments[tournamentName].players += data.get('playerName', None)

class gameResult(View):
    def post(self, request):
        global tournaments

        data = json.load(io.BytesIO(request.body))
        tournament = tournaments[data.get('tournamentName', None)]
        tournament.addGame(data.get('game', None)) # Game should be a dictionnary

def tournamentHome(request, tournamentName):
    return render(request, 'tournament/home.html', {'tournamentName': tournamentName})