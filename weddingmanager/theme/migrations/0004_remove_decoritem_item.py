# Generated by Django 4.0.8 on 2023-01-26 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_item_decoritem_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decoritem',
            name='item',
        ),
    ]