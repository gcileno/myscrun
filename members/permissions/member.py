from rest_framework import permissions

class MemberPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # Qualquer um autenticado pode listar/ver e criar (POST)
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Leitura liberada para qualquer autenticado
        if request.method in permissions.SAFE_METHODS:
            return True

        # Escrita/deleção: só admin ou o próprio dono
        return request.user.is_staff or obj.user == request.user