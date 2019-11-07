from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employee.models import Employee, Role, Group, Participation


class EmployeeAdmin(UserAdmin):
    model = Employee
    ordering = ('username',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(Group)
admin.site.register(Participation)
