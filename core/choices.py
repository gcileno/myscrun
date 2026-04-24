from django.db import models

class RoleChoices(models.TextChoices):
    OWNER = 'ow', 'Owner'
    SCRUM_MASTER = 'sm', 'Scrum Master'
    PRODUCT_OWNER = 'po', 'Product Owner'
    DEVELOPER = 'dev', 'Developer'

class OrganizationRoleChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        REJECTED = 'rejected', 'Rejected'
