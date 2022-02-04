"""Accounts filters"""

# Django 
import django_filters
from django.forms.widgets import TextInput

# Models
from . models import Order


class OrderFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(
        field_name="date_created", 
        lookup_expr="gte",
        label="Date greater than:",
        widget=TextInput(attrs={'placeholder': '  M M / D D / Y Y Y Y'})
    )

    end_date = django_filters.DateFilter(
        field_name="date_created", 
        lookup_expr="lte",
        label="Date lower than:",
        widget=TextInput(attrs={'placeholder': '  M M / D D / Y Y Y Y'})
    )

    note = django_filters.CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']