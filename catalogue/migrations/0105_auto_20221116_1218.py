# Generated by Django 2.2.13 on 2022-11-16 06:48

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0104_auto_20221116_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Who_we_are',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image')),
                ('image1', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image1')),
                ('image2', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image2')),
                ('image3', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image3')),
                ('image4', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_who_we_are_image_path, verbose_name='Image4')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Url')),
            ],
        ),
        migrations.DeleteModel(
            name='BLog',
        ),
    ]
