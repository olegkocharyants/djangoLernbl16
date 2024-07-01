# Generated by Django 5.0.6 on 2024-06-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender_choices',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=6, verbose_name='Выбор пола'),
        ),
    ]
