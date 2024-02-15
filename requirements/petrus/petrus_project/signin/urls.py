from django.urls import path
from .views import SigninView, first_connection

urlpatterns = [
    path("here/", SigninView.as_view()),
    path("", first_connection),
]
