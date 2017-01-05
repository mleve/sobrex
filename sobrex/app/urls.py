from django.conf.urls import url

from . import views
from . import data_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dorder/add$', views.dorder_add, name='dorder_add'),
    url(r'^data/address$', data_views.address, name='data_address'),
]