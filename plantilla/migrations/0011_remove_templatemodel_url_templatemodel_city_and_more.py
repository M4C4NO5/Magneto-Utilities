# Generated by Django 5.0.3 on 2024-05-22 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('plantilla', '0010_remove_templatemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatemodel',
            name='url',
        ),
        migrations.AddField(
            model_name='templatemodel',
            name='city',
            field=models.URLField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='templatemodel',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='User.magneto_user'),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]