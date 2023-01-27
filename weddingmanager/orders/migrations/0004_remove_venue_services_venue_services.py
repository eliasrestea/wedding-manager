# Generated by Django 4.0.8 on 2022-11-29 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='services',
        ),
        migrations.AddField(
            model_name='venue',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.services'),
        ),
    ]