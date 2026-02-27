from rest_framework import serializers
from organization.models import Organization
from scrun_master.serializers.projects import ProjectSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'cnpj', 'created_at', 'director', 'projects']
        read_only_fields = ['id', 'created_at', 'cnpj']