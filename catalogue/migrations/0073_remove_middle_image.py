# Generated by Django 2.2.13 on 2022-11-14 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0072_middle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='middle',
            name='image',
        ),
    ]
