from django.db import models

from employee.models import Employee, Group


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(
        Employee,
        through='ProjectParticipation',
        through_fields=('project', 'employee'),
    )
    handling_by = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class ProjectRole(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProjectParticipation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ManyToManyField(
        ProjectRole, blank=True, null=True
    )

    def __str__(self):
        return "{}-{}".format(self.project, self.employee)
