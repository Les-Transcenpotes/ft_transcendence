from django.urls import path
from . import views
from .models import UserView

urlpatterns = [
        path("get-user/", views.get_user),
        path("new-client/", views.new_client),
        path("all-client/", views.all_client),
        path("create-view/", views.create_view),
        path("add-friend/", views.add_friend),
        path("", UserView.as_view()),
]
