from core.view.viewsets import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from models import Project
from scrun_master.serializers.projects import ProjectSerializer, ProjectDetailSerializer

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    serializer_action_classes = {
        'retrieve': ProjectDetailSerializer,
        'list': ProjectSerializer,
    }

    permission_classes = [IsAuthenticated, ]