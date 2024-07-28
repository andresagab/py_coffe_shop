from django.views import generic

from products.models import Product


class ProductInfoView(generic.DetailView):
    model = Product
    template_name = "products/info_product.html"

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs["pk"])

