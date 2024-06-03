from django.contrib import admin
from .models import Product , reported_product , Category

admin.site.register(Product)
admin.site.register(reported_product)
admin.site.register(Category)