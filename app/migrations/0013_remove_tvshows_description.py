# Generated by Django 4.1.7 on 2023-04-02 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_tvshows_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshows',
            name='description',
        ),
    ]
