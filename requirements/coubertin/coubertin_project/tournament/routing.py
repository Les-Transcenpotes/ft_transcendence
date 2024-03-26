from django.urls import re_path

from tournament.classes.Consumer import Consumer

websocket_urlpatterns = [
    re_path(r"tournament/ws/(?P<roomName>[-\w]+)/$", Consumer.as_asgi()),
]