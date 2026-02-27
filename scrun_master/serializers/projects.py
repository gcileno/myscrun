from rest_framework import serializers
from models import Project, TeamMember

class ProjectSerializer(serializers.ModelSerializer):
    # Mostramos o nome da organização em vez de apenas o ID (opcional, mas ajuda o Frontend)
    organization_name = serializers.ReadOnlyField(source='organization.name')
    
    # Mostramos quem é o master de forma legível
    master_name = serializers.ReadOnlyField(source='master.user.username')

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'organization', 
            'organization_name', 'master', 'master_name', 'key'
        ]
        # O master é definido automaticamente pela View, não pelo usuário no formulário
        read_only_fields = ['id', 'master']

    def validate_key(self, value):
        """Validação personalizada para garantir que a key seja sempre maiúscula"""
        return value.upper()