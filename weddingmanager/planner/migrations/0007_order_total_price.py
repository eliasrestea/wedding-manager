# Generated by Django 4.0.8 on 2022-11-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_venue_venue_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
