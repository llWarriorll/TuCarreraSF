# Generated by Django 5.0.6 on 2024-09-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_localidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='progreso',
            field=models.IntegerField(default=0),
        ),
    ]
