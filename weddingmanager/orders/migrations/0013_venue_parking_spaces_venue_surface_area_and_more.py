# Generated by Django 4.0.8 on 2022-12-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='parking_spaces',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='surface_area',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(),
        ),
    ]
