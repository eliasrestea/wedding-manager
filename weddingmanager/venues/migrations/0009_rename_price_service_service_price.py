# Generated by Django 4.0.8 on 2022-12-28 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0008_alter_service_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='price',
            new_name='service_price',
        ),
    ]