# Generated by Django 5.0.6 on 2024-06-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_gender_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender_choices',
        ),
    ]
