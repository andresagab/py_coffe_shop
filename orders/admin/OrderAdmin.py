from django.contrib import admin

from .OrderProductInlineAdmin import OrderProductInlineAdmin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInlineAdmin
    ]


admin.site.register(Order, OrderAdmin)
