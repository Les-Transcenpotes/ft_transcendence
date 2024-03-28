from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.createTournament.as_view(), name="createTournament"),
    path("join/", views.joinTournament.as_view(), name="joinTournament"),
    path("gameResult/", views.gameResult.as_view(), name="gameresult"),
    path("home/<str:tournamentName>/", views.tournamentHome, name="tournamentHome"),
]