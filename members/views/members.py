from rest_framework import viewsets, serializers
from core.permissions.member import MemberPermission
from serializers.member import MemberSerializer
from scrun_master.models import Member

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = [MemberPermission]
    http_method_names = ['get', 'patch', 'delete']