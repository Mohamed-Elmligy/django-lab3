# Generated by Django 3.2.9 on 2021-11-05 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
