from rest_framework import viewsets, permissions
from members.models import Organization
from members.serializers.organization import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar organizações.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_url_kwarg = "id"
    
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

        if not hasattr(user, 'member'):
            return Organization.objects.none()

        return Organization.objects.filter(
            director=user.member,
                ) | Organization.objects.filter(
                    members=user.member,
                    organizationmember__is_active=True,
                )