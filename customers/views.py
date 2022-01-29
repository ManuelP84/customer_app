"""Customer views"""

# Django
from django.shortcuts import render

# Models
from . models import Customer

def customer(request, pk):
    """Customer detail view"""

    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders
    }
    return render(
        request=request, 
        template_name='customers/customer.html',
        context=context
    )


def customersList(request):
    """List all the customers"""

    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(
        request=request, 
        template_name='customers/list.html',
        context=context
    )