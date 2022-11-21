# Generated by Django 2.2.13 on 2022-08-16 13:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0059_productreview_thumbnail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('age', models.CharField(blank=True, choices=[('0-16', '0-16'), ('17-40', '17-40'), ('41-70', '41-70'), ('71-100', '71-100')], max_length=1, null=True, verbose_name='Age')),
                ('medical_condition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Medical Condition'), blank=True, null=True, size=None)),
                ('question1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Question1'), blank=True, null=True, size=None)),
                ('question2', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Question2'), blank=True, null=True, size=None)),
                ('question3', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Question3'), blank=True, null=True, size=None)),
                ('question4', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Question4'), blank=True, null=True, size=None)),
            ],
        ),
    ]