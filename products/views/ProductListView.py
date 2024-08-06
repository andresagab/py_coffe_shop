from typing import Any
from django.views.generic import ListView

from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs: Any) -> Any:
        object_list = Product.objects.filter(available=True)
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context
