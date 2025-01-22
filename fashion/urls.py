from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('signup/', views.signup, name='signup'),
    path('shop-single/', views.shopSingle, name='shop_single'),
]