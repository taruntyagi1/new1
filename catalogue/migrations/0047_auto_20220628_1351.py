# Generated by Django 2.2.13 on 2022-06-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0046_auto_20220628_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.TextField(blank=True, null=True, verbose_name='Review'),
        ),
    ]
