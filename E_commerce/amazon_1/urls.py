from django.contrib import admin
from django.urls import path
from amazon_1 import views

urlpatterns = [
    path("",views.index, name ="home"),
    path("orders",views.orders, name ="orders"),#this tells that if we goto /orders run the function=> views.py->orders
    path("cart",views.cart, name ="cart"),
    
]
