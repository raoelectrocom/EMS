from django.db import models
from django.contrib.auth.models import AbstractUser

from cities_light.models import Country, City
# from smart_selects.db_fields import ChainedForeignKey


class ProxyCountry(Country):
    class Meta:
        proxy = True

    def get_display_name(self):
        return _(self.name)

    def __str__(self):
        return _(self.name)


class ProxyCity(City):
    class Meta:
        proxy = True

    def get_display_name(self):
        return self.name

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    email = models.EmailField(
        verbose_name='email address', max_length=255,
        null=True, blank=True)
    preferred_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    description = models.TextField(blank=True)
    country = models.ForeignKey(ProxyCountry, null=True, blank=True, on_delete=models.PROTECT)
    city = models.ForeignKey(ProxyCity, null=True, blank=True, on_delete=models.PROTECT)
    zip = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username


class Permission(models.Model):
    name = models.CharField(max_length=500, unique=True)
    code_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(
        Permission, related_name="roles", null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(
        Employee,
        through='Participation',
        through_fields=('group', 'employee'),
    )

    def __str__(self):
        return self.name


class Participation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.group, self.employee)