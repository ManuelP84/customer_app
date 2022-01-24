"""Customer app URLs"""

# Django
from django.contrib import admin
from django.urls import path, include

# Views
from customer_app import views as customer_app_view


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('', include(('customers.urls', 'customers'), namespace='customers')),

    path('', include(('products.urls', 'products'), namespace='products')),

]
