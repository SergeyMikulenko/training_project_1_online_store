# Generated by Django 3.2.12 on 2022-03-16 17:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_order_delivery_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount_percent',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_sum',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.CreateModel(
            name='PromotionalOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percent', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('promotional_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('validity', models.DateField()),
                ('promotional_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotional_offer_item', to='product.item')),
            ],
        ),
    ]