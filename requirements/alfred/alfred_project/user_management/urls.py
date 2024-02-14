from django.urls import path
from . import views
from .views import newClientView

urlpatterns = [
        path("get-user/", views.get_user),
        path("new-client/", newClientView.as_view()),
        path("all-client/", views.all_client),
        path("add-friend/", views.add_friend),
]
