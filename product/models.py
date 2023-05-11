from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    minimun = models.FloatField()
    amount_per_package = models.IntegerField()
    max_availability = models.IntegerField()

    def __str__(self):
        return self.name