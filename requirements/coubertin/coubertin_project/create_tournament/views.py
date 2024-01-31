from django.shortcuts import render, redirect
from tournament.classes import Tournament
from django.contrib import messages
from tournament.views import tournaments
from .classes import BaseTournamentCreationForm


def createTournament(request):
    global tournaments
    if request.method == 'POST':
        form = BaseTournamentCreationForm(request.POST)
        if form.is_valid():
            tournamentName = form.cleaned_data.get('tournamentName')
            tournamentPass = form.cleaned_data.get('password')
            tournamentMaxPlayers = form.cleaned_data.get('maxPlayers')
            tournament = Tournament("creator", tournamentName, tournamentMaxPlayers, tournamentPass)
            tournaments[tournamentName] = tournament
            messages.success(request, f'Tournament created!')
            return redirect('tournamenthome')
    else:
        form = BaseTournamentCreationForm()
    return render(request, 'create_tournament/createForm.html', {'form': form})