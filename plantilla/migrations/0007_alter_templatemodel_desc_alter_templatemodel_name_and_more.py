# Generated by Django 5.0.3 on 2024-05-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0006_templatemodel_brand_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodel',
            name='desc',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='url',
            field=models.URLField(max_length=50, null=True),
        ),
    ]