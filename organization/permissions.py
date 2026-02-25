# scrun_core/permissions.py
from rest_framework import permissions
from .models import TeamMember

class IsScrumMaster(permissions.BasePermission):
    """
    Permissão que permite apenas a membros com papel 'sm' (Scrum Master)
    criar ou editar objetos.
    """

    def has_permission(self, request, view):
        # 1. Se for apenas leitura (GET, HEAD, OPTIONS), permitimos a qualquer membro autenticado
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # 2. Para métodos de escrita (POST, PUT, DELETE), verificamos o papel
        # Nota: Assume-se que o project_id é enviado no pedido ou na URL
        project_id = request.data.get('project') or view.kwargs.get('project_id')
        
        if not project_id:
            return False

        return TeamMember.objects.filter(
            user=request.user,
            project_id=project_id,
            role='sm'
        ).exists()