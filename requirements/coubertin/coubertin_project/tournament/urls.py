from django.urls import path
from create_tournament import views as create_views
from join_tournament import views as join_views

from . import views

urlpatterns = [
    path("failed/", views.failed, name="failed"),
    path("tournamenthome/", views.tournamentHome, name="tournamenthome"),
    path("tournamentcore/", views.tournamentCore, name="tournamentcore"),
    path('createtournament/', create_views.createTournament, name='createtournament'),
    path('jointournament/', join_views.joinTournament, name='jointournament'),
]