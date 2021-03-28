from django.contrib import admin
from .models import product, OrderItem, Order, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(product)
admin.site.register(OrderItem)
admin.site.register(Order)