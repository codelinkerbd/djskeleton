# Generated by Django 4.2.1 on 2023-05-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogcategory_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(default='bP2vgzRQ', max_length=255, verbose_name='Slug/URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='SOspXR88', max_length=255, verbose_name='Slug/URL'),
        ),
    ]
