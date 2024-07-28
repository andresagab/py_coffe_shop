from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="name")
    description = models.TextField(max_length=500, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    photo = models.ImageField(upload_to="media/logos", null=True, blank=True, verbose_name="photo")

    def __str__(self) -> str:
        return self.name

    def get_avg_rating(self):
        return self.productrating_set.aggregate(models.Avg("rating"))
