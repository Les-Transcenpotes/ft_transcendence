from django.urls import path, re_path
from . import views
from classes import PongGameConsumer

urlpatterns = [
    path("", views.pong, name="pong"),
    path("result/", views.result, name="pong-result"),
]

websocket_urlpatterns = [
    re_path(r'ws/yourpath/$', PongGameConsumer.as_asgi()),
]