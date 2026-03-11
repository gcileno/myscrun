from rest_framework import serializers
from scrun_master.models import Task
from .comment import CommentSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "status"]

class TaskDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"