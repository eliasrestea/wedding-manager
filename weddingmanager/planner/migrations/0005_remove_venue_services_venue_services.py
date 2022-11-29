# Generated by Django 4.0.8 on 2022-11-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_remove_venue_services_venue_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='services',
        ),
        migrations.AddField(
            model_name='venue',
            name='services',
            field=models.ManyToManyField(to='planner.services'),
        ),
    ]
