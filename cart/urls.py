from django.urls import path

from cart.views import CartView


urlpatterns = [
    path('', CartView.get_all, name="List all checkouts"),
    path('checkout/', CartView.create_checkout, name="Create a checkout"),
    path('checkout/update/<id>', CartView.update_checkout, name="Update a checkout"),
]