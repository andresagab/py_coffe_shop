from django.urls import path

from products.views import ProductListView, ProductListAPI, ProductInfoView

from .views import ProductFormView, ProductListView
from .views.ProductRatingFormView import ProductRatingFormView

urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('info/<int:pk>', ProductInfoView.as_view(), name="info_product"),
    path('add-product-rating', ProductRatingFormView.as_view(), name="add_product_rating"),
    path('api', ProductListAPI.as_view(), name="list_product_api"),
    path('add', ProductFormView.as_view(), name="add_product"),
]