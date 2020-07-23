from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """will return all products and including sorting and searching function"""

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """will return and views product detail"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, "products/product_detail.html", context)

