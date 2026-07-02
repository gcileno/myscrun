from django.urls import include, path
from rest_framework.routers import DefaultRouter
from members.views.me import ProfileView
from members.views.register import RegisterView
from members.views.organization import OrganizationViewSet
from members.views.invitation import InvitationView, InvitationAcceptView

router = DefaultRouter()
router.register(r"organizations", OrganizationViewSet, basename="organization")

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),

    path("", include(router.urls)),

    path("send-invitations/", InvitationView.as_view(), name="invitation"),
    path("invitations/<str:token>/accept/", InvitationAcceptView.as_view(), name="invitation-accept"),
]