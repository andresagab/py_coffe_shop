from django.contrib import admin

from .OrderProductInlineAdmin import OrderProductInlineAdmin
from ..forms import OrderForm
from ..models import Order


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    inlines = [
        OrderProductInlineAdmin
    ]


admin.site.register(Order, OrderAdmin)
