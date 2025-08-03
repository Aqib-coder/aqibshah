from django.contrib import admin
from my_projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=("project_title","project_tech","project_desc","project_image","project_slug")

admin.site.register(Project,ProjectAdmin)