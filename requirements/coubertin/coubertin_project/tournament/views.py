from django.shortcuts import render
from django.http import HttpResponse
from .models import *

################ Donnes a recuperer via les request ################

testTournament = Tournament(name = 'testTournament', maxPlayers = 8, password = 'test')
testUser1 = Player()

####################################################################

def createTournament(request):
    testTournament.save()
    return HttpResponse('Tournament created')

def addUserToTournament(request):
    testUser1.save()
    testUser1.tournament.add(testTournament)
    return HttpResponse('User added')

def startTournament(request): # Generate matches here.
    # queryset is iterable!
    pass
