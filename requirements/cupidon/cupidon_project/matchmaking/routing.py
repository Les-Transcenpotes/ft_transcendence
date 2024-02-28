from django.urls import path

from matchmaking.classes.Consumer import Consumer

# To change with domain name
websocket_urlpatterns = [
    path("matchmaking/ws/", Consumer.as_asgi()),
]