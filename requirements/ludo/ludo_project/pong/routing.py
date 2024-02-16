from django.urls import re_path

from pong.classes.Consumer import Consumer

websocket_urlpatterns = [
    re_path(r"wss://localhost:8005/ws/player1/", Consumer.as_asgi()),
]