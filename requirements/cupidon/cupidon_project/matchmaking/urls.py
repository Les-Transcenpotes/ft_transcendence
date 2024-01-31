from django.urls import path
from matchmaking import views

urlpatterns = [
    path('', views.matchmaking, name='matchmaking'),
]