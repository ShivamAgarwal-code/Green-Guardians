from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
  product = models.ForeignKey(Product , on_delete= models.CASCADE)
  buyer = models.ForeignKey(User , on_delete=models.CASCADE)
  shipping_fee = models.DecimalField(max_digits=10000 , decimal_places=2)
  ordered_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f'{self.product} - {self.buyer}'

class ReturnOrder(models.Model):
  product = models.ForeignKey(Product , on_delete= models.CASCADE)
  buyer = models.ForeignKey(User , on_delete=models.CASCADE)
  shipping_fee = models.DecimalField(max_digits=10000 , decimal_places=2)
  ordered_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f'{self.product} - {self.buyer}'


class CartOrder(models.Model):
  product = models.ForeignKey(Product , on_delete=models.CASCADE)
  buyer = models.ForeignKey(User , on_delete=models.CASCADE)
  ordered_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.product} - {self.buyer}'