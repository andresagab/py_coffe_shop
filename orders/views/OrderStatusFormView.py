from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from orders.forms import OrderStatusForm
from orders.models import Order


class OrderStatusFormView(LoginRequiredMixin, CreateView):
    template_name = 'orders/my_order.html'
    form_class = OrderStatusForm

    def form_valid(self, form):
        order = Order.objects.filter(is_active=True, user=self.request.user).first()

        # set order status
        order.status = form.instance.status
        # if order is canceled, set is_active to False
        if order.status == 'CA':
            order.is_active = False

        order.save()

        messages.success(self.request, "Order status updated successfully!")
        return HttpResponseRedirect(reverse_lazy("my_order"))

    def form_invalid(self, form):
        order = Order.objects.filter(is_active=True, user=self.request.user).first()

        messages.warning(self.request, "Failed to update order status.")
        return render(self.request, self.template_name, {'form': form, 'order': order})

    def post(self, request, *args, **kwargs):
        form = OrderStatusForm(request.POST, request=request)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
