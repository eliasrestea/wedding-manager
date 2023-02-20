# Generated by Django 4.0.8 on 2022-12-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0008_alter_service_slug'),
        ('orders', '0022_alter_order_chosen_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.venue'),
        ),
    ]
