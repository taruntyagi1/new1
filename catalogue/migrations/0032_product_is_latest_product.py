# Generated by Django 2.2.13 on 2021-04-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0031_auto_20210305_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_latest_product',
            field=models.BooleanField(default=False, verbose_name='Is Latest'),
        ),
    ]