from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.shortcuts import render

from app.mail import send_email
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


def search_order(request, tracking_number):
    query = [tracking_number]
    try:
        result = DispatchOrder.objects.get(tracking_number__contains=query)
    except:
        result = False
    response = {}
    if result:
        receiver = result.destination_address.client.name
        receiver_address = result.destination_address.street
        receiver_address = receiver_address + " " + result.destination_address.number
        receiver_address = receiver_address + " , " + result.destination_address.city
        status = result.get_last_status()
        response = {"receiver": receiver,
                    "receiver_address": receiver_address,
                    "status": status}
    return JsonResponse(response)


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


def contact(request):
    to = ['juancarlos@sobrex.cl', 'mleve@ug.uchile.cl']
    subject = 'Nuevo contacto en sobrex.cl'
    body = 'Hola, el usuario: ' + request.GET.get('name', '') + ' Envia el siguiente mensaje: \n'
    body = body + request.GET.get('message', '') + '\n'
    body = body + 'Responder a ' + request.GET.get('email')
    response = send_email(body, subject, to)
    if response == 1:
        return HttpResponse('', status=200)
    else:
        return HttpResponse('', status=400)
