from django.urls import path
from user_management.views import view_db, createUser, userProfileView, userInfoView, friendView, avatarView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("user-profile/<int:id>", userProfileView.as_view()), #ensure from petrus
        path("user-information/<int:id>", userInfoView.as_view()),
        path("friends/<int:id>", friendView.as_view()),
        path("test", createUser),
        path("view-db", view_db),
        path("avatar", avatarView.as_view()),
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
