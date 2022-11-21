# Generated by Django 2.2.13 on 2022-05-19 08:53

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0039_customertestimonial_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietitionsandnutritionists',
            name='image',
            field=models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_dietitians_image_path, verbose_name='Image'),
        ),
    ]