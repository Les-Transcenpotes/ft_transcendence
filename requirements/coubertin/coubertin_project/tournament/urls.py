from django.urls import path

from . import views

urlpatterns = [
    path("failed/", views.failed, name="failed"),
    path("tournamenthome/", views.tournamentHome, name="tournamenthome"),
    path("addusertotournament/", views.addUserToTournament, name="addusertotournament"),
    path("createtournament/", views.createTournament, name="createtournament"),
    path("starttournament/", views.startTournament, name="starttournament"),
]