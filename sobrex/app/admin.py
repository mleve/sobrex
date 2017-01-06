from django.contrib import admin

from .models import Client, Address, DispatchOrder

admin.site.register(Client)
admin.site.register(Address)
admin.site.register(DispatchOrder)