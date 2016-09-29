from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Order(models.Model):
    orderId = models.CharField(max_length = 200, primary_key=True)
    merchantId = models.CharField(max_length = 200)
    customerId =  models.CharField(max_length = 200)
    orderDate = models.DateTimeField('OrderDate')
    shipDate = models.DateTimeField('ShipDate')
    deliveryDate = models.DateTimeField('DeliveryDate')
    status = models.CharField(max_length = 200)
    items = models.TextField()

    def __str__(self):
        return self.orderId