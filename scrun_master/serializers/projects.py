from rest_framework import serializers
from scrun_master.models import Project
from .sprint import SprintSerializer
from .team import TeamMemberSerializer

class ProjectSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]
        
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

class ProjectDetailSerializer(serializers.ModelSerializer):

    team = TeamMemberSerializer(many=True, read_only=True)
    sprints = SprintSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"