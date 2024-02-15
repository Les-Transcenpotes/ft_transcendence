from django.urls import path
from .views import SigninView, TestView

urlpatterns = [
    path("here/", SigninView.as_view()),
    path("la/", TestView.as_view()),
]
