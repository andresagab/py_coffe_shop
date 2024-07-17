from typing import Any
from django.views.generic import ListView

from products.models import Product

class ProductListView(ListView):

    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"
