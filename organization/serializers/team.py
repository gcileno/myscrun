from rest_framework import serializers
from organization.models import TeamMember
from django.contrib.auth.models import User

class TeamMemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    # ou use UserSerializer se quiser mais dados
    class Meta:
        model = TeamMember
        fields = ['id', 'user', 'role']