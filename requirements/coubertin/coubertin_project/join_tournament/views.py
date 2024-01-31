from django.shortcuts import render, redirect
from tournament.classes import Player
from django.contrib import messages
from tournament.views import tournaments
from .classes import BaseTournamentJoinForm

# Create your views here.

def joinTournament(request):
    global tournaments
    if request.method == 'POST':
        form = BaseTournamentJoinForm(request.POST)
        if form.is_valid():
            tournamentName = form.cleaned_data.get('tournamentName')
            if tournamentName in tournaments:
                tournamentPass = form.cleaned_data.get('password')
                if tournaments[tournamentName].password == tournamentPass:
                    newPlayer = Player('test') # Need to get the nickname here !
                    tournaments[tournamentName].addPlayer(newPlayer)
                    messages.success(request, f'Tournament joined!')
                    return redirect('tournamenthome')
                else:
                    messages.error(request, f'Wrong password')
            else:
                messages.error(request, f'Tournament does not exist')
    else:
        form = BaseTournamentJoinForm()
    return render(request, 'create_tournament/createForm.html', {'form': form})