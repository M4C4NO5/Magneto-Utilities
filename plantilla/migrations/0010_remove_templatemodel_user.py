# Generated by Django 5.0.3 on 2024-05-22 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0009_templatemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatemodel',
            name='user',
        ),
    ]
