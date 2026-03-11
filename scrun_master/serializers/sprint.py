from rest_framework import serializers
from scrun_master.models import Sprint
from .task import TaskSerializer

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = "__all__"

class SprintDetailSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Sprint
        fields = "__all__"