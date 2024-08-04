from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from orders.forms import OrderProductForm
from orders.models import Order, OrderProduct


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

        # if product already in order, update quantity
        if form.instance.product and OrderProduct.objects.filter(order=order, product=form.instance.product).exists():
            order_product = order.orderproduct_set.get(product=form.instance.product)
            print(order_product)
            order_product.quantity += form.instance.quantity
            order_product.save()

            messages.success(self.request, f"Product added successfully to order #{order.id}!")
            return HttpResponseRedirect(reverse_lazy("my_order"))
        else:
            form.save()

            messages.success(self.request, f"Product added successfully to order #{order.id}!")
            return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Failed to add product to order.")
        return super().form_invalid(form)