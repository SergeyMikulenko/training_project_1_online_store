# Generated by Django 3.2.12 on 2022-03-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_order_delivery_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildeliverynotification',
            name='hour_before_delivery',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]