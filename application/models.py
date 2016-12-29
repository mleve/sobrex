from __future__ import unicode_literals
from django.db import models
#from jsonfield import JSONField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import base64

""" 
Description: Models Aplication Solunova Api
Developer: ctroc@qin.cl , christopher.troc@gmail.com
"""

class Client(models.Model):
    """
    Relationship one to many companies
    """
    rut = models.CharField('rut',max_length= 20)
    name = models.CharField('Name',max_length=100)
    email = models.EmailField('email')
    phone = models.CharField('phone',max_length=20)    
    def __unicode__(self):
      return self.name


class Adress(models.Model):
    """
    Description: data table for Companies
    RelatioShip: one to one User model
    """
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Client,on_delete=models.CASCADE, related_name='receiver')

    street = models.CharField('street', max_length=100)
    number = models.CharField('number',max_length=10)
    sub_index = models.CharField('sub_index', max_length=10)
    city = models.CharField('city',max_length=20)
    zipcode = models.CharField('zipcode', max_length=20)    

    def __unicode__(self):
      return self.name + " "+self.number


class Status(models.Model):
    name = models.CharField('name',max_length=20)

class DispatchOrder(models.Model):

    payment_charge = models.CharField('payment_charge',max_length=10)
    value = models.IntegerField('value')
    creation = models.DateTimeField('creation_date',auto_now_add=True)
    tracking_number = ArrayField(
        models.CharField(max_length=20))
    status = models.ManyToManyField(Status,
        through = 'OrderStatus')


class OrderStatus(models.Model):
    dispatch_order = models.ForeignKey(DispatchOrder, on_delete = models.CASCADE)
    status = models.ForeignKey(Status,on_delete = models.CASCADE)
    date_time = models.DateTimeField('date_time', auto_now_add=True)



