from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="%Y/%m/%d")


class Bucket(models.Model):
    items = models.ManyToManyField(Item, related_name="item_bucket", through="product.BucketItems")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()


class BucketItems(models.Model):
    count = models.PositiveIntegerField(default=0)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE, related_name="bucket_items_bucket")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bucket_items_item")


class Discount(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name="discount_item")
    discount_percent = models.PositiveIntegerField(default=0)


def add_item_discount(signal, sender, instance, created, update_fields, raw, using, **kwargs):
    if created:
        Discount.objects.create(item_id=instance.id, discount_percent=0)


models.signals.post_save.connect(add_item_discount, sender=Item)

