# Generated by Django 2.2.13 on 2022-11-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0088_blog_image4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='how_it_work',
            name='image',
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='heading2',
            field=models.TextField(blank=True, null=True, verbose_name='Heading2'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='heading3',
            field=models.TextField(blank=True, null=True, verbose_name='Heading3'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='title2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Title2'),
        ),
        migrations.AddField(
            model_name='how_it_work',
            name='title3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Title3'),
        ),
    ]
