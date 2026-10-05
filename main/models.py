from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 100)
    brand = models.CharField(max_length= 50)
    size = models.CharField(max_length= 15)
    color = models.CharField(max_length= 45)
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
