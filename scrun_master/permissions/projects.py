from rest_framework import permissions
from scrun_master.models import TeamMember

class IsProjectScrumMaster(permissions.BasePermission):
    """
    Permite criação de tasks apenas se o utilizador for o SM do projeto.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            project_id = request.data.get('project')
            return TeamMember.objects.filter(
                member__user=request.user,
                project_id=project_id,
                role='sm'
            ).exists()
        return True
    
class IsProjectMaster(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 'obj' aqui seria o Projeto ou o TeamMember sendo editado
        if hasattr(obj, 'master'): # Se for o Projeto
            return obj.master.user == request.user
        if hasattr(obj, 'project'): # Se for o TeamMember
            return obj.project.master.user == request.user
        return False