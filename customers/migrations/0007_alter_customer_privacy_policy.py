# Generated by Django 4.0.1 on 2022-02-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_customer_privacy_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='privacy_policy',
            field=models.BooleanField(editable=False),
        ),
    ]
