from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

from core.choices import OrganizationRoleChoices
from members.models import Invitation
from members.services.invitation_service import send_invitation_email
from core.permissions.projects import IsProjectScrumMasterOrOwner, IsProjectMaster
from members.serializers.invitation import InvitationCreateSerializer


class InvitationView(APIView):
    #permission_classes = [IsAuthenticated, IsProjectScrumMasterOrOwner | IsProjectMaster]

    def get(self, request):
        pass
    
    def post(self, request):
        serializer = InvitationCreateSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        invitation = serializer.save()

        # Send email logic goes here (e.g., using Django's send_mail or a third-party service)
        send_invitation_email(invitation)
        

        return Response({"message": "Invitation sent successfully"}, status=201)

class InvitationAcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, token):
        # Logic to accept the invitation using the token
        invitation = self.get_object_or_404(Invitation, token=token)
        if invitation.status != OrganizationRoleChoices.PENDING:
            return Response({"error": "Invitation is not valid"}, status=400)
        
        if invitation.email != request.user.email:
            return Response({"error": "You are not authorized to accept this invitation"}, status=403)

        # This would typically involve validating the token, updating the invitation status,
        # and adding the user to the organization or project as needed.
        return Response({"message": "Invitation accepted successfully"}, status=200)