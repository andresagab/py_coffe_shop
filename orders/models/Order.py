from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=2, null=False, default='UC', verbose_name="status")
    order_date = models.DateTimeField(auto_now_add=True)

    # Product status
    STATUS_TYPES = (
        # Unconfirmed
        {
            'key': 'UC',
            'color': 'indigo',
            'name': 'Unconfirmed',
        },
        # Confirmed
        {
            'key': 'CO',
            'color': 'sky',
            'name': 'Confirmed',
        },
        # Delivered
        {
            'key': 'DE',
            'color': 'orange',
            'name': 'Delivered',
        },
        # Paid
        {
            'key': 'PA',
            'color': 'green',
            'name': 'Paid',
        },
        # Canceled
        {
            'key': 'CA',
            'color': 'red',
            'name': 'Canceled',
        }
    )

    def __str__(self) -> str:
        return f"order {self.id} by {self.user}"
    
    @admin.display(description="Total")
    def get_total(self):
        total = 0
        for order_product in self.orderproduct_set.all():
            total += order_product.get_subtotal()
        return total

    @admin.display(description="Status")
    def get_status(self, key: str = "name"):
        status = [status for status in self.STATUS_TYPES if status['key'] == self.status]

        # if status is not empty and key is None, then return dict
        if status and key is None:
            return status[0]
        # else, if status is not empty and key is not None, then return specified value
        elif status and key is not None:
            return status[0][key]
        else:
            return None
