from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from orders.models import Order


class MyOrderView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = "orders/my_order.html"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()

    def get_context_data(self, **kwargs):
        # get order
        order = self.get_object()
        # set context
        context = super().get_context_data(**kwargs)
        context["order"] = order
        
        if order is not None:
            context["order_status"] = order.get_status(key=None)
        else:
            context["order_status"] = None

        return context
