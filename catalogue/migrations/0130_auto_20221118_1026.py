# Generated by Django 2.2.13 on 2022-11-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0129_auto_20221118_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame5',
            name='choice',
            field=models.CharField(choices=[('our_mission', 'our_mission'), ('our_vision', 'our_vision')], max_length=30, verbose_name='Choice'),
        ),
    ]