from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'fashionHTML/index.html')


def shop(request):
    return render(request,'fashionHTML/shop.html')

def cart(request):
    return render(request,'fashionHTML/cart.html')

def contact(request):
    return render(request,'fashionHTML/contact.html')
