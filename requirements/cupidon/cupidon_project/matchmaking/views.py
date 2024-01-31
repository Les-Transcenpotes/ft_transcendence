from django.shortcuts import render

# Create your views here.
def matchmaking(request):
    return render(request, 'matchmaking/matchmaking.html', {})