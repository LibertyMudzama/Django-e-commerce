from django.shortcuts import render, get_object_or_404
from .models import product, Category, ParentCategory
# Create your views here.



def product_list(request):
    context = {
        'products': product.objects.all()
    }
    return render(request, 'index.html', context)



def product_detail(request , slug):
    Product = product.objects.get(slug=slug)
    categories = ParentCategory.objects.all()
    context = {
        'product': Product,
        'categories': categories
    }
    return render(request, 'detail.html', context)



def category_detail(request, slug):
    category = get_object_or_404(ParentCategory, slug = slug)
    return render(request, 'category-full.html')



def navbar_details(request):
    categories = ParentCategory.objects.all()
    names = ['liberty', 'Mudzama']
    context = {
        'categories': categories,
        'nmaes': names
    }
    return render(request, 'navbar.html', context)
