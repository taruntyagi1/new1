# Generated by Django 2.2.13 on 2022-05-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0036_dietitionsandnutritionists'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietitionsandnutritionists',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
