from django.urls import re_path

from classes import PongGameConsumer

websocket_urlpatterns = [
    re_path(r"ws/pong/(?P<room_name>\w+)/$", PongGameConsumer.as_asgi()),
]