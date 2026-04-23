from rest_framework import viewsets
from serializers.member import MemberSerializer
from scrun_master.models import Member

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

