# Generated by Django 2.2.13 on 2022-11-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0091_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='how_it_work',
            name='main_title',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Main_Title'),
        ),
    ]
