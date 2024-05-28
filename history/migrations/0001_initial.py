# Generated by Django 5.0.3 on 2024-05-22 19:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantilla', '0009_templatemodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_image', models.ImageField(upload_to='vacancies/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('template', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plantilla.templatemodel')),
            ],
        ),
    ]
