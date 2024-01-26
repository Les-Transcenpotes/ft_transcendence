from django.urls import re_path

from . import players

websocket_urlpatterns = [
    re_path(r"ws/pong/(?P<room_name>\w+)/$", players.PongPlayer.as_asgi()),
]