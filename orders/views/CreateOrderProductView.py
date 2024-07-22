from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from orders.forms import OrderProductForm
from orders.models import Order


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    """
    When the form is valid, save the form data to the database.
    """
    def form_valid(self, form):
        # get order instance
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        # set form order instance to store it
        form.instance.order = order
        form.instance.quantity = 1
        form.save()

        return super().form_valid(form)
