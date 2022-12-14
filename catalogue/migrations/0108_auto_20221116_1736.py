# Generated by Django 2.2.13 on 2022-11-16 12:06

import catalogue.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0107_auto_20221116_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, help_text='Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers', null=True, upload_to=catalogue.models.get_client_logo_image_path, verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_logo_product', to='catalogue.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='our_products',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='our_products_product', to='catalogue.Product'),
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
