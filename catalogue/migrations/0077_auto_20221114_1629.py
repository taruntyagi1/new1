# Generated by Django 2.2.13 on 2022-11-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0076_how_it_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='how_it_work',
            name='heading1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Heading1'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='heading2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Heading2'),
        ),
    ]
