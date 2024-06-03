from django.shortcuts import render , HttpResponse , redirect 
from rest_framework.viewsets import ModelViewSet
from .models import CartOrder
from .serializer import CartOrderSerializer
from product.models import Product


def cartpostview(request , id):
  if request.method == 'POST':
    print(request.user)
    print(id)
    item = Product.objects.get(pk=id)
    obj = CartOrder(buyer=request.user , product=item)
    obj.save()
    return HttpResponse(status=204)