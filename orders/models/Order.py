from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"order {self.id} by {self.user}"

    def get_total(self):
        total = 0
        for order_product in self.orderproduct_set.all():
            total += order_product.get_subtotal()
        return total