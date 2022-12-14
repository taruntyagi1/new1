# Generated by Django 2.2.13 on 2022-06-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0045_productreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='timestamp',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='productreview',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='HyperLink'),
        ),
    ]
