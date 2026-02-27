from rest_framework import serializers
from organization.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'user', 'organization']
        read_only_fields = ['id']

class MemberDetailSerializer(serializers.ModelSerializer):

    organization = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    teams= serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['id', 'user', 'organization', 'role']
        read_only_fields = ['id']