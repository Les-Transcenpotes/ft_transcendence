from django.urls import path
from .views import signinView, signupView, refreshView, view_db

urlpatterns = [
    path("view-db", view_db),
    path("signin/<str:string>", signinView.as_view()),
    path("signup", signupView.as_view()),
    path("JWT_refreshment", refreshView.as_view())
]
