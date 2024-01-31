from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .classes import *

################ Donnes a recuperer via les request ################

testUser1 = Player(id = 0)
testTournament = Tournament(creator = testUser1.name, name = 'testTournament', maxPlayers = 8, password = 'test')

####################################################################

tournaments = {}

def tournamentHome(request): #Essayer de retourner la reponse en json
    global tournaments
    return JsonResponse()

def tournamentCore(request): # Generate matches here.
    global tournaments
    if request.method == 'POST':
        tournamentName = 'test' # Il faut reussir a le get
        tournament = tournaments[tournamentName]
        players = tournament.players
        while (players.len() > 1):
            for i in range(0, players.len(), 2):
                pass # Lancer un match entre i et i + 1
    # Quand qqn perd un match on le retire de la liste et on relance une fois que tous les matchs d'une ronde sont termines
            
def failed(request):
    return HttpResponse("Whatever you're doing isn't fucking working")