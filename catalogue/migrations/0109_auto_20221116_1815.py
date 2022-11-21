# Generated by Django 2.2.13 on 2022-11-16 12:45

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0108_auto_20221116_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_products',
            name='image',
            field=models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_our_products_image_path, verbose_name='Image'),
        ),
    ]