from members.models import Organization

def get_user_organizations(user):
    return (
        Organization.objects
        .filter(members__user=user)
        .distinct()
    )