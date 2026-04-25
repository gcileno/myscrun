from django.db import models
from core import settings
from authentication.models import User

from core.choices import OrganizationRoleChoices, RoleChoices


class Member(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='member'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

class OrganizationMember(models.Model):
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE
    )

    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('organization', 'member')

class Organization(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    director = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='directed_organizations',
        )
    
    members = models.ManyToManyField(Member, through=OrganizationMember, related_name='organizations')

    def __str__(self):
        return f"{self.name} - {self.cnpj}"


class Invitation(models.Model):
    email = models.EmailField()

    invited_by = models.ForeignKey(Member, on_delete=models.CASCADE)

    # destino do convite
    organization = models.ForeignKey(
        Organization, null=True, blank=True, on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        'scrun_master.Project', null=True, blank=True, on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices= RoleChoices.choices,
        null=True, 
        blank=True)

    status = models.CharField(
        max_length=20,
        choices= OrganizationRoleChoices.choices,
        default=OrganizationRoleChoices.PENDING
    )

    token = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
