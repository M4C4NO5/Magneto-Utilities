# Generated by Django 4.2.11 on 2024-05-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0002_remove_templatemodel_font_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
