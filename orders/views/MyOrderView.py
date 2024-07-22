from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from orders.models import Order


class MyOrderView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = "orders/my_order.html"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()
