from django.contrib import admin
from .models import Member, Organization, OrganizationMember, Invitation


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    search_fields = ("name", "user__username")

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cnpj", "director", "created_at")
    search_fields = ("name", "cnpj")

@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "member", "is_active")
    search_fields = ("organization__name", "member__name")

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "invited_by", "organization")
    search_fields = ("email", "invited_by__name", "organization__name")
