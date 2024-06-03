from django.contrib import admin
from .models import Order , ReturnOrder , CartOrder

admin.site.register(Order)
admin.site.register(ReturnOrder)
admin.site.register(CartOrder)