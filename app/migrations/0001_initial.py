# Generated by Django 4.1.7 on 2023-03-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='img')),
                ('details', models.CharField(max_length=100)),
                ('budget', models.PositiveIntegerField()),
                ('box_office', models.PositiveIntegerField()),
                ('desicription', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tvshows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='img')),
                ('details', models.CharField(max_length=100)),
                ('budget', models.PositiveIntegerField()),
                ('box_office', models.PositiveIntegerField()),
                ('desicription', models.TextField(max_length=1000)),
            ],
        ),
    ]
