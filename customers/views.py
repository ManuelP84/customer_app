"""Customer views"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Models
from . models import Customer

# Filters
from accounts.filters import OrderFilter

# Decorators
from users.decorators import allowed_users


@login_required
def customer(request, pk):
    """Customer detail view"""

    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'myFilter': myFilter
    }
    return render(
        request=request, 
        template_name='customers/customer.html',
        context=context
    )


@login_required
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


@login_required
@allowed_users(allowed_roles=['customers'])
def userPage(request):
    """User view"""

    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    total_orders_pending = orders.filter(status="Pending").count()
    total_orders_delivered = orders.filter(status="Delivered").count()

    context = {
        'orders': orders,
        'total_orders_pending': total_orders_pending,
        'total_orders': total_orders,
        'total_orders_delivered': total_orders_delivered
    }

    return render(
        request=request, 
        template_name='users/user.html', 
        context=context
    )