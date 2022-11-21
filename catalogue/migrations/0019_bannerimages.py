# Generated by Django 2.2.9 on 2020-01-31 17:35

import catalogue.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_auto_20200122_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=catalogue.models.get_banner_image_path, verbose_name='Banner Image')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('hyperlink', models.URLField(blank=True, null=True, verbose_name='HyperLink')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
    ]
