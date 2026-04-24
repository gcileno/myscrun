from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

from core.choices import OrganizationRoleChoices
from members.models import Invitation
from core.permissions.projects import IsProjectScrumMasterOrOwner, IsProjectMaster
from members.serializers.invitation import InvitationCreateSerializer


class InvitationView(APIView):
    #permission_classes = [IsAuthenticated, IsProjectScrumMasterOrOwner | IsProjectMaster]

    def get(self, request):
        # Rota para testar o envio de email simples
        send_mail(
            subject='Test Email',
            message='This is a test email from Django.',
            from_email='gabriel_cileno@hotmail.com',
            recipient_list=['gabriel.cileno53@gmail.com']
        )
        return Response({"message": "Test email sent successfully"}, status=200)

    def post(self, request):
        serializer = InvitationCreateSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        invitation = serializer.save()

        # Send email logic goes here (e.g., using Django's send_mail or a third-party service)
        send_mail(
            subject='You are invited to join a project',
            message=f'You have been invited to join the project. Use the following token to accept the invitation: {invitation.token}',
            from_email='noreply@yourdomain.com',
            recipient_list=[invitation.email]
        )

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