# Generated by Django 5.0.3 on 2024-05-14 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0003_alter_templatemodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatemodel',
            name='font',
            field=models.CharField(default='Sans-serif', max_length=30),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='color',
            field=models.CharField(default='#fff', max_length=30),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='desc',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='title',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
