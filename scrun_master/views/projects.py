from core.choices import RoleChoices
from core.view.viewsets import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from members.models import Member
from scrun_master.models import Project, TeamMember
from scrun_master.permissions.projects import IsProjectScrumMasterOrOwner
from scrun_master.serializers.projects import ProjectSerializer, ProjectDetailSerializer

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    serializer_action_classes = {
        'retrieve': ProjectDetailSerializer,
        'list': ProjectSerializer,
    }

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [IsAuthenticated()]
        # update, partial_update, destroy
        return [IsProjectScrumMasterOrOwner()]

    def perform_create(self, serializer):
        member = Member.objects.get(user=self.request.user)

        project = serializer.save(master=member)

        TeamMember.objects.create(
            member=member,
            project=project,
            role=RoleChoices.OWNER
        )