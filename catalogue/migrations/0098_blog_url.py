# Generated by Django 2.2.13 on 2022-11-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0097_middle_main_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='HyperLink'),
        ),
    ]
