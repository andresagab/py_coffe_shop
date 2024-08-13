from django.contrib import admin

from .OrderProductInlineAdmin import OrderProductInlineAdmin
from ..forms import OrderForm
from ..models import Order


class OrderAdmin(admin.ModelAdmin):
    # data table
    list_display = [
        'id',
        'user',
        'is_active',
        'get_total',
        'get_status',
    ]

    # form
    form = OrderForm
    inlines = [
        OrderProductInlineAdmin
    ]


admin.site.register(Order, OrderAdmin)
