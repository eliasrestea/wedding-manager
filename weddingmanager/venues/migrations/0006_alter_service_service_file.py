# Generated by Django 4.0.8 on 2022-12-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0005_alter_venue_venue_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_file',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
