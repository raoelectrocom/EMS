# Generated by Django 2.2.7 on 2019-11-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20191129_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participation',
            old_name='person',
            new_name='employee',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='code_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]