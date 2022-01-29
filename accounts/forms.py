
# Django
from django.forms import ModelForm

# Models
from accounts.models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'       # Another way is to set the list with the fields: ['customer','product','status']
        


