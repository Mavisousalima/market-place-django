from django.urls import path

from product.views import ProductView


urlpatterns = [
    path('product', ProductView.get_all, name="List all products"),
    path('product/<name>', ProductView.get_by_name, name="Get a product"),
    path('product/create/', ProductView.create_product, name="Create a product"),
    path('product/delete/<id>', ProductView.delete_product, name="Delete a product"),
    path('product/update/<id>', ProductView.update_product, name="Update a product")
]