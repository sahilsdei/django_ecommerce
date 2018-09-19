from django.db import models
from products.models import Products
# Create your models here.
class Cart (models.Model):
    user = models.IntegerField(default=0)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self):
        return self.user