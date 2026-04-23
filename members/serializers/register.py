from rest_framework import serializers
from django.contrib.auth import get_user_model

from members.models import Member

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    member_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'member_name']

    def create(self, validated_data):
        member_name = validated_data.pop('member_name')  # separa antes de criar o User
        user = User.objects.create_user(**validated_data)
        Member.objects.create(user=user, name=member_name)
        return user