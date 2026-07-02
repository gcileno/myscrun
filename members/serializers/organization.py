from rest_framework import serializers
from members.models import Organization
from scrun_master.serializers.projects import ProjectSerializer

class OrganizationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name"]
        
class OrganizationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'cnpj', 'created_at', 'director', 'projects']
        read_only_fields = ['id', 'created_at', 'director']

    def create(self, validated_data):
        request = self.context.get('request')

        if request is not None and hasattr(request.user, 'member'):
            validated_data['director'] = request.user.member

        return super().create(validated_data)