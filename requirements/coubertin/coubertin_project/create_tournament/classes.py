from django import forms

class BaseTournamentCreationForm(forms.Form):
    tournamentName = forms.CharField(label='tournamentName', max_length=50)
    maxPlayers = forms.IntegerField(max_value=64, min_value=4)
    password = forms.CharField(label='password', max_length=20)
