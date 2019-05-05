from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    path('card/', views.HomePageView.as_view(), name='card'),
]
