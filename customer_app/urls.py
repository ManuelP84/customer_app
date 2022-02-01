"""Customer app URLs"""

# Django
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


# Views
from customer_app import views as customer_app_view


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),

    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('', include(('customers.urls', 'customers'), namespace='customers')),

    path('', include(('products.urls', 'products'), namespace='products')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
