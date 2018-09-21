from django.db import models

# Create your models here.
class Product (models.Model):
    name=models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    created=  models.DateTimeField('created date')
    updated_date=models.DateTimeField('updated date')
    def __str__(self):
        return self.name