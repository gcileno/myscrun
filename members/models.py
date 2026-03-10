from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Member(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')

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

    invited = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    invited_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)

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



