from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Client, Address, DispatchOrder
from django.http import JsonResponse
from django.core import serializers


def address(request):
    client_id = request.GET.get('client_id', '-1')
    if client_id != -1:
        addresses = Address.objects.filter(client=client_id)
    else:
        addresses = Address.objects.all()
    response = serializers.serialize("json", addresses)
    return JsonResponse(response, safe=False)


def dispatch_order(request):
    pick_up = request.POST.get('pick_up_address', -1)
    destination = request.POST.get('destination_address', -1)
    charge = request.POST.get('payment_charge', -1)
    value = request.POST.get('value', -1)
    tracking_numbers = request.POST.get('tracking_number','')
    tracking_numbers = tracking_numbers.split(',')

    new_order = DispatchOrder(
        pick_up_address_id=pick_up,
        destination_address_id=destination,
        payment_charge=charge,
        value=value,
        tracking_number=tracking_numbers
    )

    #response = 'ok'
    #return HttpResponse(tracking_numbers)
    try:
        new_order.full_clean()
        new_order.save()
        return HttpResponse('created')
    except (ValidationError, ValueError) as e:
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
        return HttpResponse(tracking_numbers, status=400)

