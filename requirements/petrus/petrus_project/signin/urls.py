from django.urls import path
from .views import SigninView

urlpatterns = [
    path("here/", SigninView.as_view()),
]
