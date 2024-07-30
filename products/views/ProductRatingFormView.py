from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from products.forms import ProductRatingForm


class ProductRatingFormView(LoginRequiredMixin, CreateView):
    template_name = "products/info_product.html"
    form_class = ProductRatingForm

    def get_success_url(self):
        return reverse_lazy("info_product", kwargs={"pk": self.object.product.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        messages.success(self.request, "Rating added successfully!")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Failed to add rating.")
        return render(self.request, self.template_name, {'form': form, 'product': form.instance.product})
        #return HttpResponseRedirect(reverse_lazy("info_product", kwargs={"pk": form.instance.product.id}))
        #return super().form_invalid(form)
