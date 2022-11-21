# Generated by Django 2.2.9 on 2020-04-02 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_terms_and_conditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='mobile number')),
                ('password', models.CharField(blank=True, max_length=6, null=True, verbose_name='password')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('purpose', models.CharField(blank=True, choices=[('MV', 'Mobile Verification'), ('LO', 'Login')], max_length=2, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
