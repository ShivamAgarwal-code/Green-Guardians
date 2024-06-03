from django.urls import path
from rest_framework import routers
from .views import cartpostview

urlpatterns = [
  path( 'cart/<int:id> ' , cartpostview , name='cart'),
]