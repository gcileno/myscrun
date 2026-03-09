from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Member(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')


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
    
    members = models.ManyToManyField(Member, related_name='organizations')
    
    def __str__(self):
        return self.name



