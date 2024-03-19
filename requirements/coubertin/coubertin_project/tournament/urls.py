from django.urls import path

from . import views

urlpatterns = [
    path("start/<str:tournamentName>/", views.startTournament, name="startTournament"),
    path("create/", views.createTournament, name="createTournament"),
    path("join/", views.joinTournament, name="joinTournament"),
    path("/home/<str:tournamentName>/", views.tournamentHome, name="tournamentHome"),
]