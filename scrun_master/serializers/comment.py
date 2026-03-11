from rest_framework import serializers
from scrun_master.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Comment
        fields = ["author", "content", "created_at"]
