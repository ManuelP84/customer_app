"""Products Views"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Models
from products.models import Product

# Decorators
from users.decorators import allowed_users


@login_required
@allowed_users(allowed_roles=['admin'])
def products(request):
    """Products view"""

    products = Product.objects.all()
    context =  {'products': products}
    return render(request, 'products/product.html', context)
