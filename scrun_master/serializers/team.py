from rest_framework import serializers
from scrun_master.models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = "__all__"