from rest_framework import serializers
from members.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name']
        
class MeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    organizations = OrganizationSimpleSerializer(many=True)
    projects = ProjectSimpleSerializer(many=True)