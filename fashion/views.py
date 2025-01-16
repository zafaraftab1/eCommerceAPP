from django.shortcuts import render
from .models import fashionCategory

# Create your views here.
def home(request):
    category1= fashionCategory()
    category1.name="Gray Shoe"
    category1.price= 18.25
    return render(request,'fashionHTML/index.html', {'category1' : category1})

def shop(request):
    return render(request,'fashionHTML/shop.html')

def cart(request):
    return render(request,'fashionHTML/cart.html')

def contact(request):
    return render(request,'fashionHTML/contact.html')

def thankyou(request):
    return render(request,'fashionHTML/thankyou.html')
