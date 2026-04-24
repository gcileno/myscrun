from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def send_invitation_email(invitation):
    link = f"http://localhost:3000/invite/accept?token={invitation.token}"

    html_content = render_to_string(
        'templates/emails/invitation.html',
        {
            'organization_name': invitation.organization.name if invitation.organization else '',
            'project_name': invitation.project.name if invitation.project else '',
            'invitation_link': link,
        }
    )

    email = EmailMultiAlternatives(
        subject="Você foi convidado 🚀",
        body="Você foi convidado para um projeto.",
        from_email="noreply@yourdomain.com",
        to=[invitation.email],
    )

    email.attach_alternative(html_content, "text/html")
    email.send()