from django.urls import path
from members.views.me import ProfileView
from members.views.register import RegisterView
from members.views.invitation import InvitationView, InvitationAcceptView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),

    path("send-invitations/", InvitationView.as_view(), name="invitation"),
    path("invitations/<str:token>/accept/", InvitationAcceptView.as_view(), name="invitation-accept"),
]