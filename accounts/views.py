"""Accounts views"""

# Django
from django.shortcuts import render, redirect
from django.template import context

# Models
from accounts.models import Order
from customers.models import Customer

# Forms
from . forms import OrderForm


def account(request):
    """Account view"""

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders_pending = orders.filter(status="Pending").count()
    total_orders_delivered = orders.filter(status="Delivered").count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders_pending': total_orders_pending,
        'total_orders_delivered': total_orders_delivered
    }


    return render(
        request=request, 
        template_name='accounts/dashboard.html',
        context=context
    )


def createOrder(request):
    """Create order view"""
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:accounts')
    else:
        form = OrderForm()

    context={'form': form}

    return render(
        request=request,
        template_name='accounts/order_form.html',
        context=context
    )

def updateOrder(request, pk):
    """Update order view"""

    order = Order.objects.get(id=pk)
    

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)        
        if form.is_valid():
            form.save()
            return redirect('accounts:accounts')
    else:
        form = OrderForm(instance=order)

    context={'form': form}

    return render(
        request=request,
        template_name='accounts/order_form.html',
        context=context
    )


def deleteOrder(request, pk):
    """Delete order view"""

    order = Order.objects.get(id=pk)
    context = {'order': order}

    if request.method == 'POST':
        order.delete()
        return redirect('accounts:accounts')

    return render(
        request=request,
        template_name='accounts/delete_order.html',
        context=context
    )

