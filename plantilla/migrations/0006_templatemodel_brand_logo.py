# Generated by Django 5.0.3 on 2024-05-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0005_templatemodel_font_color_alter_templatemodel_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatemodel',
            name='brand_logo',
            field=models.ImageField(null=True, upload_to='brand_logos/'),
        ),
    ]
