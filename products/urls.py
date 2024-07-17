from django.urls import path

from products.views import ProductListView

from .views import ProductFormView, ProductListView

urlpatterns = [
    path('add/', ProductFormView.as_view(), name="add_product"),
    path('', ProductListView.as_view(), name="list_product"),
]