# Generated by Django 2.2.13 on 2022-07-19 07:22

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220719_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, help_text='Please Upload a file in jpg, jpeg, png format only', null=True, upload_to=accounts.models.get_profile_picture, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['JPEG', 'PNG', 'JPG'])], verbose_name='Profile Picture'),
        ),
    ]
