# Generated by Django 5.0.3 on 2024-05-17 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0007_alter_templatemodel_desc_alter_templatemodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodel',
            name='desc',
            field=models.CharField(default='N/A', max_length=500),
        ),
    ]