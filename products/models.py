from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} by {self.brand} at ${self.price}"