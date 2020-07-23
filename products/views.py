from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    """will return all products and including sorting and searching function"""

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "products/products.html", context)
    