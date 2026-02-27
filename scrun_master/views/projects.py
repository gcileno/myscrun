from rest_framework import viewsets
from models import Project
from organization.models import Member

class ProjectViewSet(viewsets.ModelViewSet):
    # ...
    def perform_create(self, serializer):
        # 1. Busca o 'Member' correspondente ao utilizador logado
        member = Member.objects.get(user=self.request.user)
        # 2. Salva o projeto definindo este membro como Master
        serializer.save(master=member)