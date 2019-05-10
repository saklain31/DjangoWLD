from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

#from rest_framework import routers
from userData.views import *

#router = routers.DefaultRouter()
#router.register(r'tempOrder', tempOrderViewSet)

urlpatterns = [
    #path(r'', include(router.urls)),
    path('', Test.saveTempOrder),
    #path('chooseDenim/',getJeans1),
]
