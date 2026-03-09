from rest_framework import serializers
from members.models import OrganizationMember
from scrun_master.serializers.projects import ProjectSerializer

class OrganizationMemberSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField()
    member = serializers.StringRelatedField()
    projects = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationMember
        fields = ['id', 'organization', 'member', 'invited', 'accepted', 'is_active', 'invited_at', 'accepted_at', 'projects']
        read_only_fields = ['id', 'invited_at', 'accepted_at']

    def get_projects(self, obj):
        return ProjectSerializer(obj.organization.project_set.all(), many=True).data