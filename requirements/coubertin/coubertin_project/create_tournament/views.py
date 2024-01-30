from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from tournament.classes import Tournament
from django.contrib import messages
from tournament.views import tournaments


def createTournament(request):
    global tournaments
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            tournamentName = form.cleaned_data.get('username')
            tournamentPass = form.cleaned_data.get('password')
            tournamentMaxPlayers = 8
            tournament = Tournament(tournamentName, tournamentMaxPlayers, tournamentPass)
            tournaments[tournamentName] = tournament
            messages.success(request, f'Tournament created!')
            return redirect('tournamenthome')
    else:
        form  = UserCreationForm()
    return render(request, 'create_tournament/createForm.html', {'form': form})