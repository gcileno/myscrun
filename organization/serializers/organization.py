from rest_framework import serializers
from organization.models import Organization
from organization.serializers.projects import ProjectSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'projects']
        read_only_fields = ['id', 'created_at', 'updated_at']