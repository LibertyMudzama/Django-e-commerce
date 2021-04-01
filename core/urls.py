from django.urls import path
from . views import product_list, product_detail,category_detail

app_name = 'core'

urlpatterns= [
    path('', product_list, name='product_list'),
    path('product/category/<slug>',category_detail, name="category_details"),
    path('product/<slug>', product_detail, name="product_detail"),
    
]