from django import forms

class BaseTournamentJoinForm(forms.Form):
    tournamentName = forms.CharField(label='tournamentName', max_length=50)
    password = forms.CharField(label='password', max_length=20)