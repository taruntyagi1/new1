# Generated by Django 2.2.13 on 2022-11-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0131_auto_20221118_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='footer',
            field=models.CharField(blank=True, choices=[('Left_section', 'Left_section'), ('Quick_links', 'Quick_links'), ('More_links', 'More_links'), ('Contact_us', 'Contact_us')], max_length=1000, null=True, verbose_name='Footer'),
        ),
    ]
