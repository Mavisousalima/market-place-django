from django.db import models

from product.models import Product


class CartProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Product: {self.product.name}, quantity: {self.quantity}"

    def get_total_price(self):
        return self.quantity * self.product.price


class Cart(models.Model):
    products = models.ManyToManyField(CartProduct)

    def get_total(self):
        total = 0
        for cart_product in self.products.all():
            total += cart_product.get_total_price()
        return total