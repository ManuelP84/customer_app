"""Users signals"""

# Django
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from customers.models import Customer
from django.contrib.auth.models import Group


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            privacy_policy=True
        )
    print("Profile created!")

post_save.connect(customer_profile, sender=User)