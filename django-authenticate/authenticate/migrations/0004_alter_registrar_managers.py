# Generated by Django 5.1.4 on 2025-01-09 18:45

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='registrar',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
