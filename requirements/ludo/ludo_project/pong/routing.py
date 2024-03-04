from django.urls import re_path

from pong.classes.Consumer import Consumer

websocket_urlpatterns = [
    re_path(r"pong/ws/(?P<roomName>\w+)/$", Consumer.as_asgi()),
]