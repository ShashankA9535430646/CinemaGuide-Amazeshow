# Generated by Django 4.1.7 on 2023-04-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_movies_rating_alter_tvshows_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='tvshows',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=1, null=True),
        ),
    ]