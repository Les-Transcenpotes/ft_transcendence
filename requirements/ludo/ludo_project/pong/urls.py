from django.urls import path
from . import views

urlpatterns = [
    path("<str:roomName>/", views.pong, name="pong"),
]
