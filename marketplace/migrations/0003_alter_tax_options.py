# Generated by Django 5.0.6 on 2024-07-12 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name_plural': 'tax'},
        ),
    ]