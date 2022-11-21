# Generated by Django 2.2.13 on 2022-11-17 12:21

import catalogue.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0121_auto_20221117_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_about_us_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame1_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Frame2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_about_us_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame2_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Frame3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_about_us_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame3_product', to='catalogue.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Frame4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_about_us_image_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame4_product', to='catalogue.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='About_us',
        ),
    ]