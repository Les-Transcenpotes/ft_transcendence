from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.pong, name="pong"),
    path("result/", views.result, name="pong-result"),
]
