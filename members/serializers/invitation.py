from rest_framework import serializers
from uuid import uuid4
from django.utils import timezone
from datetime import timedelta

from members.models import Invitation
from core.choices import OrganizationRoleChoices

class InvitationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = ['email', 'organization', 'project', 'role']

    def validate(self, data):
        if not data.get('organization') and not data.get('project'):
            raise serializers.ValidationError(
                "Você deve informar organization ou project"
            )
        return data

    def create(self, validated_data):
        request = self.context['request']

        invitation = Invitation.objects.create(
            **validated_data,
            invited_by=request.user.member,
            token=uuid4().hex,
            status=OrganizationRoleChoices.PENDING,
            expires_at=timezone.now() + timedelta(days=7)
        )

        return invitation