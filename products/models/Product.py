from datetime import timedelta, date

from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="name")
    description = models.TextField(max_length=500, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    photo = models.ImageField(upload_to="media/logos", null=True, blank=True, verbose_name="photo")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

    def get_avg_rating(self):
        return self.productrating_set.aggregate(models.Avg("rating")).get("rating__avg")

    def still_new(self):
        still = False
        # if model has created_at, and it is less than 60 days
        if self.created_at and (self.created_at.date() + timedelta(days=60)) >= date.today():
            still = True

        return still
