from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  category_name = models.CharField(max_length=200)

  def __str__(self):
    return self.category_name




class Product(models.Model):
  product_name = models.CharField(max_length=200)
  category = models.ForeignKey(Category , on_delete=models.CASCADE ,  null=True)
  seller = models.ForeignKey(User , on_delete= models.CASCADE)
  product_description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10000 , decimal_places=2)
  product_image = models.ImageField(null = True)
  verification_doc = models.ImageField(null = True)
  is_approved = models.BooleanField(default=False)
  listed_at = models.DateField(auto_now_add=True)
  image_link = models.CharField(max_length=1000 , null=True)

  def __str__(self):
    return f'{self.product_name} - {self.seller}'
  

class reported_product(models.Model):
  Product = models.OneToOneField(Product , on_delete= models.CASCADE)
  is_banned = models.BooleanField(default=False)
  reported_by = models.ForeignKey(User , on_delete=models.CASCADE)
  reported_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f'{self.Product}  ,Product status :  {self.is_banned}'