# Generated by Django 2.2.13 on 2022-11-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0078_how_it_work_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='how_it_work',
            name='heading1',
        ),
        migrations.RemoveField(
            model_name='how_it_work',
            name='heading2',
        ),
        migrations.AddField(
            model_name='middle',
            name='heading1',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Heading1'),
        ),
    ]
