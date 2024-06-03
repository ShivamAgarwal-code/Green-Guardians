from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from product.models import Product 
from django.contrib.auth import authenticate , login , logout
from message.models import ContactMsg
from order.models import CartOrder
from django.contrib.auth.decorators import login_required

def home_view(request):
  obj = Product.objects.filter(is_approved=True)
  context = {
    'obj':obj
  }
  return render(request , 'home.html' , context)

def login_view(request):
  if request.method == 'POST':
    print(request.POST)
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    user = authenticate(request , username = username , password = password)
    if user is not None:
      login(request , user)
      return redirect('home')
    else:
      return redirect('login')
  else:
   return render(request , 'login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def about_view(request):
  return render(request , 'about.html')

def contact_view(request):
  if request.method == 'POST':
    print(request.POST)
    user_name = request.POST.get('Name')
    user_contact = request.POST.get('Contact')
    user_email = request.POST.get('Email')
    user_msg = request.POST.get('Msg')
    print(user_name , user_contact , user_email , user_msg)
    obj = ContactMsg(name=user_name ,contact=user_contact , email=user_email , msg=user_msg )
    obj.save()
    return redirect('home')
  else:
   return render(request , 'contact.html')

def product_view(request , id):
  obj = Product.objects.get(pk=id)
  content = {
    'obj': obj
  }
  return render(request , 'product.html' , content)

@login_required(login_url='login')
def cart_view(request):
  total = 0
  obj = CartOrder.objects.filter(buyer=request.user)
  for item in obj:
    total += item.product.price
  content = {
    'obj':obj,
    'total': total,
  }
  return render(request , 'cart.html' , content)