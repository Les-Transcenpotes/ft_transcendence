from django.http import JsonResponse
from django.urls import path
from memory.views import (
        tournamentView,
        gameView,
        playerView,
)


def view_db(request):
    return JsonResponse({"\"db\"": "nothing is in db"})


urlpatterns = [
    path("view-db", view_db),
    path("pong/tournaments/<int:id>", tournamentView.as_view()),
    path("pong/matchs/<int:id>", gameView.as_view()),
    path("players/<int:id>", playerView.as_view()),
]
