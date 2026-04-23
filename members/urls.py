from django.urls import path
from members.views.me import ProfileView
from members.views.register import RegisterView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
]