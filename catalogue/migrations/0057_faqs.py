# Generated by Django 2.2.13 on 2022-07-23 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0056_auto_20220723_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_faqs', to='catalogue.Product')),
            ],
        ),
    ]
