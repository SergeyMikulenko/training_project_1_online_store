# Generated by Django 4.0.2 on 2022-03-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_delivery_date_order_delivery_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email_hours_before_delivery',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
