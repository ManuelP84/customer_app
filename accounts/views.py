"""Accounts views"""

# Django
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

# Models
from accounts.models import Order
from customers.models import Customer

# Forms
from . forms import OrderForm

# Decorators
from users.decorators import allowed_users, admin_only


@login_required
@admin_only
def account(request):
    """Account view"""

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_orders_pending = orders.filter(status="Pending").count()
    total_orders_delivered = orders.filter(status="Delivered").count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_orders_pending': total_orders_pending,
        'total_orders_delivered': total_orders_delivered
    }


    return render(
        request=request, 
        template_name='accounts/dashboard.html',
        context=context
    )


@login_required
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    """Create order view"""

    OrderFormSet = inlineformset_factory(
        parent_model=Customer, 
        model=Order,
        max_num=1,
        fields=('product', 'status')
    )    
    customer = Customer.objects.get(id=pk)
    
    if request.method == 'POST':
        formset = OrderFormSet(
            request.POST,             
            instance=customer
        )
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('accounts:accounts')
    else:
    #   form = OrderForm(initial={'customer': customer})
        formset = OrderFormSet(
            instance=customer, 
            queryset=Order.objects.none()
        )

    context={'formset': formset}

    return render(
        request=request,
        template_name='accounts/order_form.html',
        context=context
    )


@login_required
@allowed_users(allowed_roles=['admin'])
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


@login_required
@allowed_users(allowed_roles=['admin'])
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

