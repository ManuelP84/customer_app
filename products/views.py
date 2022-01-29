"""Products Views"""

# Django
from django.shortcuts import render

# Models
from products.models import Product

def products(request):
    """Products view"""

    products = Product.objects.all()
    context =  {'products': products}
    return render(request, 'products/product.html', context)
