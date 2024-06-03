from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10000, decimal_places=2)