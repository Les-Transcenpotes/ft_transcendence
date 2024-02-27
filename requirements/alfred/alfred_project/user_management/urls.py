from django.urls import path
from user_management.views import createUserView, all_client

urlpatterns = [
        path("create-user", createUserView.as_view()),
        path("personal-info", all_client),
        path("id/<int:id>", all_client),
]
