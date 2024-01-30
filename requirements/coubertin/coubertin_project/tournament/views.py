from django.shortcuts import render
from django.http import HttpResponse
from .classes import *

################ Donnes a recuperer via les request ################

testTournament = Tournament(name = 'testTournament', maxPlayers = 8, password = 'test')
testUser1 = Player(name = 'Brieuc')

####################################################################

tournaments = {}

def createTournament(request):
    tournaments['testTournament'] = testTournament
    return HttpResponse('Tournament created')

def addUserToTournament(request):
    return HttpResponse('User added')

def startTournament(request): # Generate matches here.
    pass
