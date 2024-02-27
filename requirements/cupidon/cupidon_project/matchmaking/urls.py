<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
=======
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.matchmaking, name="matchmaking"),
>>>>>>> e2ea298601bf4635088ec57dd5491828c932dce8
]