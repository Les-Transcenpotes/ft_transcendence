from django.urls import re_path

from .classes import PongGameConsumer

websocket_urlpatterns = [
    re_path(r"wss://www.test.com/socketserver", PongGameConsumer.as_asgi()),
]