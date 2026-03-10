from django.contrib import admin
from .models import Project, TeamMember, Sprint ,Task, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "member", "role")
    search_fields = ("project__name", "member__name")

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "name", "start_date", "end_date")
    search_fields = ("project__name", "name")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "sprint", "title", "status", "assigned_to")
    search_fields = ("sprint__project__name", "title")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "author", "content", "created_at")
    search_fields = ("task__sprint__project__name", "author__name", "content")


