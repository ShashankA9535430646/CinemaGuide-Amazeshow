# Generated by Django 4.1.7 on 2023-04-01 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_movies_rating_alter_tvshows_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshows',
            name='box_office',
        ),
    ]
