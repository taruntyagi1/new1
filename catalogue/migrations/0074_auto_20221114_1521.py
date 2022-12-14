# Generated by Django 2.2.13 on 2022-11-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0073_remove_middle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='middle',
            name='heading',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='Heading'),
        ),
    ]
