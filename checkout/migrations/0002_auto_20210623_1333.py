# Generated by Django 2.2.13 on 2021-06-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='rz_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='rz_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
