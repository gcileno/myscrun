from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='projects')
    key = models.CharField(max_length=10, help_text="Ex: SCRUN-01")

    def __str__(self):
        return f"{self.key} - {self.name}"

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('sm', 'Scrum Master'),
        ('po', 'Product Owner'),
        ('dev', 'Developer'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'project')