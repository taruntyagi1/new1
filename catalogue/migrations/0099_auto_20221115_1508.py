# Generated by Django 2.2.13 on 2022-11-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0098_blog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietitionsandnutritionists',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Url'),
        ),
    ]