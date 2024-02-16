from django.urls import path
from .views import checkInView, refreshJWTView, refreshTokenView, view_db
from myjwt.decorator import ensure_JWT, ensure_refresh_token

urlpatterns = [
    path("", ensure_JWT(refreshJWTView.as_view())),
    path("check/<str:type>/<str:data>", checkInView.as_view()),
    path("refresh-token", ensure_refresh_token(refreshTokenView.as_view())),
    path("view-db", view_db)
]
