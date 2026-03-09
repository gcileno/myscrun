from rest_framework import viewsets, permissions
from models import Organization
from serializers.organization import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar organizações.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
    # Define as permissões: Autenticado para ver, mas podes restringir a escrita
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Opcional: Filtrar para que o utilizador veja apenas a organização 
        onde ele é o diretor ou membro.
        """
        user = self.request.user
        # Se não for staff/admin, vê apenas onde está vinculado
        if user.is_staff:
            return Organization.objects.all()
        return Organization.objects.filter(director=user)