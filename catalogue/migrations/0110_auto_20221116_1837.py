# Generated by Django 2.2.13 on 2022-11-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0109_auto_20221116_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='who_we_are',
            name='url',
        ),
        migrations.AddField(
            model_name='who_we_are',
            name='Hyperlink',
            field=models.URLField(blank=True, null=True, verbose_name='Hyperlink'),
        ),
    ]
