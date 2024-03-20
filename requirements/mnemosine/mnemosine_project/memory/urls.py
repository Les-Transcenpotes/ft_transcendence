from django.http import JsonResponse
from django.urls import path
from memory.views import (
        tournamentView,
        userTournamentView,
        matchView,
        userMatchView,
        playerView,
        userPlayerView
)


def view_db(request):
    return JsonResponse({"\"db\"": "nothing is in db"})


urlpatterns = [
    path("view-db", view_db),
    path("tournament", tournamentView.as_view()),
    path("view-tournament", userTournamentView.as_view()),
    path("match", matchView.as_view()),
    path("view-match", userMatchView.as_view()),
    path("player", playerView.as_view()),
    path("view-player", userPlayerView.as_view()),
]
