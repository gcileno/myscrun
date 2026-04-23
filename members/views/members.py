from rest_framework import viewsets, serializers
from members.permissions.member import MemberPermission
from serializers.member import MemberSerializer
from scrun_master.models import Member

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    permission_classes = [MemberPermission]

    def perform_create(self, serializer):
        # Garante 1 member por usuário
        if hasattr(self.request.user, 'member'):
            raise serializers.ValidationError("Você já possui um perfil de membro.")
        serializer.save(user=self.request.user)