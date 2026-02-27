from django.db import models
from django.contrib.auth import get_user_model
from organization.models import Organization
from organization.models import Member

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='projects')
    master = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='project_master')
    key = models.CharField(max_length=10, help_text="Ex: SCRUN-01")

    def __str__(self):
        return f"{self.key} - {self.name}"

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('ow', 'Owner'),
        ('sm', 'Scrum Master'),
        ('po', 'Product Owner'),
        ('dev', 'Developer'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='team_memberships')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('member', 'project')

class Sprint(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sprints')
    start_date = models.DateField()
    end_date = models.DateField()
    goal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('code_review', 'Code Review'),
        ('blocked', 'Blocked'),
        ('test', 'Test'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, related_name='tasks')
    
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='assigned_tasks')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hours_required = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    block_reason = models.TextField(blank=True, null=True)
    
    points = models.IntegerField(default=0)

    PRIORITY_CHOICES = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.user.username} on {self.task.title}'