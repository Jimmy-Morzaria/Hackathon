from django.shortcuts import render
from django.template import loader

from .models import Order

def index(request):
    order_list = Order.objects.all()
    context = {
        'order_list': order_list,
    }
    return render(request, 'orders/index.html', context)