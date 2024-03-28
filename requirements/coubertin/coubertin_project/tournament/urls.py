from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.createTournament, name="createTournament"),
    path("join/", views.joinTournament, name="joinTournament"),
    path("/gameResult/", views.gameResult, name="gameresult"),
    path("/home/<str:tournamentName>/", views.tournamentHome, name="tournamentHome"),
]