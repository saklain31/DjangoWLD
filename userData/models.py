# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tempOrder(models.Model):
    orderID = models.CharField(max_length=30) 
    userID = models.CharField(max_length=30) 
    gmail = models.EmailField()
    name = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    jeans1_1 = models.CharField(max_length=60)
    jeans1_2 = models.CharField(max_length=60)
    jeans1_3 = models.CharField(max_length=30)
    jeans2_1 = models.CharField(max_length=60)
    jeans2_2 = models.CharField(max_length=60)
    jeans2_3 = models.CharField(max_length=30)

    def __str__(self):
        return self.name


