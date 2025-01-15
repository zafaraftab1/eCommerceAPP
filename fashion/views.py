from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'fashionHTML/index.html', {'price' : '100'})

def shop(request):
    return render(request,'fashionHTML/shop.html')

def cart(request):
    return render(request,'fashionHTML/cart.html')

def contact(request):
    return render(request,'fashionHTML/contact.html')

def thankyou(request):
    return render(request,'fashionHTML/thankyou.html')
