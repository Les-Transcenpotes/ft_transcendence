from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def createTournament(request):
    form  = UserCreationForm()
    return render(request, 'create_tournament/createForm.html', {'form': form})