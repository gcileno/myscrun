from rest_framework import viewsets, exceptions
from models import Project, Member, TeamMember
from scrun_master.permissions.projects import IsProjectMaster
from scrun_master.serializers.projects import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [IsProjectMaster, ]

    def perform_create(self, serializer):
        # 1. Verificar se o utilizador é membro da organização do projeto
        organization_id = self.request.data.get('organization')
        try:
            member = Member.objects.get(user=self.request.user, organization_id=organization_id)
        except Member.DoesNotExist:
            raise exceptions.PermissionDenied("You must be a member of the organization to create a project.")

        # 2. Guardar o projeto definindo o master automaticamente
        project = serializer.save(master=member)

        # 3. Adicionar automaticamente o master à tabela de TeamMember como Scrum Master (opcional)
        TeamMember.objects.get_or_create(
            member=member,
            project=project,
            defaults={'role': 'sm'}
        )