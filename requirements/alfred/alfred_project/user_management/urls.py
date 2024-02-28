from django.urls import path
from user_management.views import createUserView, personalInfoView, all_client, createUser

urlpatterns = [
        path("create-user", createUserView.as_view()),
        path("personal-info", personalInfoView.as_view()),
        path("id/<int:id>", all_client),
        path("test", createUser),
        path("view-db", all_client)
]
