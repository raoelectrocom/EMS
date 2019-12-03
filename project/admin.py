from django.contrib import admin

from project.models import Project, ProjectRole, ProjectParticipation


admin.site.register(Project)
admin.site.register(ProjectRole)
admin.site.register(ProjectParticipation)
