from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Client, Address, DispatchOrder, OrderStatus, Status
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
    tracking_numbers = request.POST.get('tracking_number', '')
    tracking_numbers = tracking_numbers.split(',')

    new_order = DispatchOrder(
        pick_up_address_id=pick_up,
        destination_address_id=destination,
        payment_charge=charge,
        value=value,
        tracking_number=tracking_numbers
    )

    # response = 'ok'
    # return HttpResponse(tracking_numbers)
    try:
        new_order.full_clean()
        new_order.save()
        initial_status = Status.objects.get(name="en oficina")
        OrderStatus.objects.create(status=initial_status, dispatch_order=new_order)
        return HttpResponse('created', status=201)
    except (ValidationError, ValueError) as e:
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
        return HttpResponse(tracking_numbers, status=400)


def create_client(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    rut = request.POST.get('rut')
    email = request.POST.get('email')

    new_client = Client(
        name=name,
        phone=phone,
        rut=rut,
        email=email
    )
    try:
        new_client.full_clean()
        new_client.save()
        display = ""
        display += new_client.rut
        display += " - "
        display += new_client.name
        return JsonResponse({'id': new_client.pk, 'display': display})
    except ValidationError as e:
        return JsonResponse(e, status=400)


def create_client_address(request):
    street = request.POST.get('street')
    number = request.POST.get('number')
    sub_index = request.POST.get('sub_index')
    city = request.POST.get('city')
    zipcode = request.POST.get('zipcode')
    client_id = request.POST.get('client_id')

    new_address = Address(
        street=street,
        number=number,
        sub_index=sub_index,
        city=city,
        zipcode=zipcode,
        client_id=client_id,
    )
    try:
        new_address.full_clean()
        new_address.save()
        display = ""
        display += new_address.street
        display += " "
        display += new_address.number
        return JsonResponse({'id': new_address.pk, 'display': display})
    except ValidationError as e:
        return JsonResponse(e, status=400)
