# Generated by Django 3.2.12 on 2022-03-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20220306_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
