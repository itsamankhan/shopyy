from django.contrib import admin
from .models import (
    Customer, 
    Product, 
    Cart, 
    OrderPlaced
)


@admin.register(Customer)
class CustormerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'description', 'category', 'brand', 'image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer', 'product', 'ordered_date', 'quantity', 'status']