# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tempOrder(models.Model):
    orderID = models.CharField(max_length=30)
    email = models.EmailField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    thread1 = models.CharField(max_length=60)
    denim1 = models.CharField(max_length=60)
    cut1 = models.CharField(max_length=30)
    denim2 = models.CharField(max_length=60)
    thread2 = models.CharField(max_length=60)
    cut2 = models.CharField(max_length=30)
    prevMeasurement = models.CharField(max_length=30)
    tailorId = models.CharField(max_length=30)
    dateOfMeasurement = models.CharField(max_length=30)
    timeOfMeasurement = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	
    def __str__(self):
        return self.firstname


class order(models.Model):
    orderID = models.CharField(max_length=30)
    email = models.EmailField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    thread1 = models.CharField(max_length=60)
    denim1 = models.CharField(max_length=60)
    cut1 = models.CharField(max_length=30)
    denim2 = models.CharField(max_length=60)
    thread2 = models.CharField(max_length=60)
    cut2 = models.CharField(max_length=30)
    prevMeasurement = models.CharField(max_length=30)
    tailorId = models.CharField(max_length=30)
    dateOfMeasurement = models.CharField(max_length=30)
    timeOfMeasurement = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    paymentType= models.CharField(max_length=30)
    paymentId = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname


