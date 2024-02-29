from django.urls import path
from user_management.views import createUserView, personalInfoView, all_client, createUser, clientInfoIdView, friendView

urlpatterns = [
        path("create-user", createUserView.as_view()),
        path("personal-info", personalInfoView.as_view()),
        path("user-info/<int:id>", clientInfoIdView.as_view()),
        path("add-friend/<int:id>", friendView.as_view()),
        path("test", createUser),
        path("view-db", all_client)
]
