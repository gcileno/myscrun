from rest_framework import serializers
from organization.models import Project
from organization.serializers.team import TeamMemberSerializer

class ProjectSerializer(serializers.ModelSerializer):
    team = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'key', 'name', 'description', 'team']