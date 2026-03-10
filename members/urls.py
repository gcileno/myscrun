from django.urls import path
from members.views.me import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
]