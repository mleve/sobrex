from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext

from app.models import Client, DispatchOrder

@login_required
def index(request):
    orders = DispatchOrder.objects.all().order_by("-pk")
    return render(request, 'app/index.html',{'orders' : orders})


@login_required
def dorder_add(request):
    clients = Client.objects.all()
    dispatch_orders = DispatchOrder.objects.all()
    tracking_array = []
    for order in dispatch_orders:
        tracking_array.extend(order.tracking_number)

    return render(request, 'app/dorder/add.html', {'clients': clients, 'tracking_array': tracking_array})


def to_login(request):
    return render(request, 'app/login.html')


def logs_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'app/login.html', {'error:' 'Credenciales incorrectas'})


def logout_view(request):
    logout(request)
    return redirect("/")
