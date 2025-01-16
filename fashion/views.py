from django.shortcuts import render
from .models import fashionCategory

# Create your views here.
def home(request):
    categories = fashionCategory.objects.all()
    return render(request,'fashionHTML/index.html', {'category1' : categories})

def shop(request):
    return render(request,'fashionHTML/shop.html')

def cart(request):
    return render(request,'fashionHTML/cart.html')

def contact(request):
    return render(request,'fashionHTML/contact.html')

def thankyou(request):
    return render(request,'fashionHTML/thankyou.html')
