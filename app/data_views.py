
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Client, Address
from django.http import JsonResponse
from django.core import serializers

def address(request):
	client_id = request.GET.get('client_id','-1')
	if client_id != -1:
		addresses = Address.objects.filter(Client = client_id)
	else:
		addresses = Address.objects.all()
	response = serializers.serialize("json",addresses)
	return JsonResponse(response,safe = False)
