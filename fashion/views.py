from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'fashionHTML/index.html')


def shop(request):
    return render(request,'fashionHTML/shop.html')
