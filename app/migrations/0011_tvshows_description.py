# Generated by Django 4.1.7 on 2023-04-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_tvshows_box_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshows',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
