# Generated by Django 2.2.13 on 2022-06-28 06:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0044_product_product_rating_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Review')),
                ('rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_product', to='catalogue.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
