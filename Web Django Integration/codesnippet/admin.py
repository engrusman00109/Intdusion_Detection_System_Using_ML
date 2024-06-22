from django.contrib import admin
from .models import (
    Section,
    CodeSnippet,
    ProjectOutput,
    Student,
    Supervisor,
    Team,
    ResearchPaper,
)

# Register your models here.


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["id", "section", "title"]


@admin.register(ProjectOutput)
class ProjectOutputAdmin(admin.ModelAdmin):
    list_display = ["id", "section", "output_name"]


@admin.register(Supervisor)
class SuperVisorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "project_title"]


@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
