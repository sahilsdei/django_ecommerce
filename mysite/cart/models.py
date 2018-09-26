from django.db import models
from product.models import Product
from datetime import datetime
# Create your models here.
class Cart (models.Model):
    user = models.IntegerField(default=0)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    def __str__(self):
        return self.product.name