from rest_framework import serializers
from scrun_master.models import TeamMember
from .projects import ProjectSimpleSerializer

class TeamMemberSerializer(serializers.ModelSerializer):
    project = ProjectSimpleSerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = "__all__"