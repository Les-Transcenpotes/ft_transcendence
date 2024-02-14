from django.urls import path
from . import views
from .views import newClientView

urlpatterns = [
        path("new-client/", newClientView.as_view()),
        path("all-client/", views.all_client),
]
