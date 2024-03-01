from django.urls import path
from user_management.views import createUserView, personalInfoView, view_db, createUser, clientInfoIdView, friendView

urlpatterns = [
        path("create-user", createUserView.as_view()),
        path("personal-info", personalInfoView.as_view()),
        path("user-info/<int:id>", clientInfoIdView.as_view()),
        path("friends/<int:id>", friendView.as_view()),
        path("test", createUser),
        path("view-db", view_db)
]
