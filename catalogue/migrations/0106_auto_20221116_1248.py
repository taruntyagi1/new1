# Generated by Django 2.2.13 on 2022-11-16 07:18

import catalogue.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0105_auto_20221116_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('main_heading', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Main_Heading')),
                ('image', models.ImageField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_blog_image_path, verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_product', to='catalogue.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
