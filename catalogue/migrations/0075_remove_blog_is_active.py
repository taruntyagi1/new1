# Generated by Django 2.2.13 on 2022-11-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0074_auto_20221114_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_active',
        ),
    ]