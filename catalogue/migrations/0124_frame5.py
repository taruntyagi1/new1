# Generated by Django 2.2.13 on 2022-11-17 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0123_auto_20221117_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('choice', models.CharField(choices=[('Our mission', 'Our mission'), ('Our vision ', 'Our vision')], max_length=30, verbose_name='Choice')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frame5_product', to='catalogue.Product')),
            ],
        ),
    ]