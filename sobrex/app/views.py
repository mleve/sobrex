from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from app.models import Client


def index(request):
    return render(request, 'app/index.html')


def dorder_add(request):
    clients = Client.objects.all()
    return render(request, 'app/dorder/add.html', {'clients': clients})
