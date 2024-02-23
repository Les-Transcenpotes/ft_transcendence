from django.urls import path

from pong.classes.Consumer import Consumer

# To change with domain name
websocket_urlpatterns = [
    path("pong/ws/", Consumer.as_asgi()),
]