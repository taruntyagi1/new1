# Generated by Django 2.2.13 on 2022-11-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0092_how_it_work_main_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='how_it_work',
            name='main_title',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Main_Title'),
        ),
        migrations.AlterField(
            model_name='how_it_work',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='how_it_work',
            name='title2',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title2'),
        ),
        migrations.AlterField(
            model_name='how_it_work',
            name='title3',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title3'),
        ),
        migrations.AlterField(
            model_name='middle',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Title'),
        ),
    ]
