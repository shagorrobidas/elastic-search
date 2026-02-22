from django.urls import path
from products.views import ProductSearchView, product_list_view

urlpatterns = [
    path(
        'api/products/',
        ProductSearchView.as_view(),
        name='product-search-api'
    ),
    path(
        '',
        product_list_view,
        name='product-list'
    ),
]