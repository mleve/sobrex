from django.conf.urls import url

from . import views
from . import data_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.to_login, name='to_login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^logs_in/$', views.logs_in, name='login_user'),
    url(r'^dorder/add$', views.dorder_add, name='dorder_add'),
    url(r'^data/address$', data_views.address, name='data_address'),
    url(r'^data/dispatch_order$', data_views.dispatch_order, name='data_dispatch_order'),
    url(r'^data/create_client$', data_views.create_client, name='data_create_client'),
    url(r'^data/create_client_address$', data_views.create_client_address, name='data_create_client_address'),
]