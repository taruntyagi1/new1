# Generated by Django 2.2.13 on 2022-11-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0124_frame5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame5',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Description'),
        ),
    ]
