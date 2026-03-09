from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from members.serializers.member import MeSerializer

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        member = request.user.member

        organizations = member.organizations.filter(
            organizationmember__is_active=True,
            organizationmember__accepted=True
        )

        projects = member.projects.all()

        data = {
            "id": member.id,
            "name": member.name,
            "organizations": organizations,
            "projects": projects,
        }

        serializer = MeSerializer(data)

        return Response(serializer.data)