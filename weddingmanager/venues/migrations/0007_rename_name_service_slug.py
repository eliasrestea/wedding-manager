# Generated by Django 4.0.8 on 2022-12-23 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0006_alter_service_service_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='slug',
        ),
    ]
