# -*- coding: utf-8 -*-
from django.db import migrations


def create_superuser(apps, schema_editor):
    # Get models
    User = apps.get_model('auth', 'User')

    if not User.objects.filter(email='admin@example.com').exists():
        # Create the default database
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="admin123456",
            username="site_admin"
        )


def remove_superuser(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    User = apps.get_model('auth', 'User')

    # Delete the default homepage
    # Page and Site objects CASCADE
    User.objects.filter(email='admin@example.com').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser),
    ]
