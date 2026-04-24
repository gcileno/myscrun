from core.view.viewsets import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from models import TeamMember
from core.permissions.projects import IsProjectScrumMasterOrOwner, IsProjectMaster
from scrun_master.serializers.team import TeamMemberSerializer

class TeamMemberViewSet(BaseViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    permission_classes = [IsAuthenticated & (IsProjectScrumMasterOrOwner | IsProjectMaster), ]