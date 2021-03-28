from django.shortcuts import render
from .models import product
# Create your views here.

def product_list(request):
    context={
        'products': product.objects.all()
    }
    return render(request,'index.html',context)