from rest_framework import permissions
from rest_framework import permissions
from core.choices import RoleChoices
from scrun_master.models import Project
from scrun_master.models import TeamMember
from members.models import Member


class IsProjectScrumMasterOrOwner(permissions.BasePermission):
    """
    Permite escrita apenas para Scrum Masters do projeto.
    """

    def has_permission(self, request, view):

        # leitura liberada para autenticados
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        project_id = (
            request.data.get("project") or
            view.kwargs.get("project_pk") or
            view.kwargs.get("project_id")
        )

        if not project_id:
            return False

        member = Member.objects.filter(user=request.user).first()

        if not member:
            return False

        return TeamMember.objects.filter(
            member=member,
            project_id=project_id,
            role__in=[RoleChoices.SCRUM_MASTER, RoleChoices.OWNER]
        ).exists()
    
class IsProjectMaster(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 'obj' aqui seria o Projeto ou o TeamMember sendo editado
        if hasattr(obj, 'master'): # Se for o Projeto
            return obj.master.user == request.user
        if hasattr(obj, 'project'): # Se for o TeamMember
            return obj.project.master.user == request.user
        return False