# Generated by Django 2.2.13 on 2022-11-14 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0079_auto_20221114_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='middle',
            name='heading1',
        ),
    ]
