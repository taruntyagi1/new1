# Generated by Django 2.2.13 on 2022-11-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0095_auto_20221115_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='main_heading',
            field=models.TextField(blank=True, null=True, verbose_name='Main_Heading'),
        ),
    ]
