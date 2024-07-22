from django.db import models

from orders.models import Order
from products.models import Product


class OrderProduct(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"

    def get_subtotal(self):
        return self.quantity * self.product.price
