# Generated by Django 2.2.13 on 2022-11-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0102_remove_middle_main_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='how_it_work',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='how_it_work',
            name='heading2',
        ),
        migrations.RemoveField(
            model_name='how_it_work',
            name='heading3',
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='description2',
            field=models.TextField(blank=True, null=True, verbose_name='Description2'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='description3',
            field=models.TextField(blank=True, null=True, verbose_name='Description3'),
        ),
    ]
