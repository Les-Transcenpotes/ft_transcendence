from django.urls import path
from .views import checkInView, refreshJWTView, refreshTokenView, view_db, bad

urlpatterns = [
    path("", refreshJWTView.as_view()),
    path("check/<str:type>/<str:data>", checkInView.as_view()),
    path("refresh-token", refreshTokenView.as_view()),
    path("view-db", view_db),
    path("bad", bad)
]
