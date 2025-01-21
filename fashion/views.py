from django.shortcuts import render
from .models import fashionCategory

# Create your views here.
def home(request):
    categories = fashionCategory.objects.all()
    return render(request,'fashionHTML/index.html', {'category1' : categories})

def shop(request):
    categories = fashionCategory.objects.all()
    return render(request,'fashionHTML/shop.html',{'category1' : categories})

def cart(request):
    return render(request,'fashionHTML/cart.html')

def contact(request):
    return render(request,'fashionHTML/contact.html')

def thankyou(request):
    return render(request,'fashionHTML/thankyou.html')

def signup(request):
    return render(request,'fashionHTML/signin_signup.html')
