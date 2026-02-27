from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    director = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='directed_organizations')
    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE, related_name='members')

    class Meta:
        unique_together = ('user', 'organization')

