# Generated by Django 2.2.13 on 2022-11-15 06:24

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0085_auto_20221115_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_blog_image_path, verbose_name='Image2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image2',
            field=models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_blog_image_path, verbose_name='Image3'),
        ),
    ]
