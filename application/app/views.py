from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from app.models import Client, DispatchOrder


def index(request):
    orders = DispatchOrder.objects.all()
    return render(request, 'app/index.html',{'orders' : orders})


def dorder_add(request):
    clients = Client.objects.all()
    dispatch_orders = DispatchOrder.objects.all()
    tracking_array = []
    for order in dispatch_orders:
        tracking_array.extend(order.tracking_number)

    return render(request, 'app/dorder/add.html', {'clients': clients, 'tracking_array': tracking_array})
