from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nosotros/', views.nosotros),
    path('servicio/', views.servicio),
    path('contacto/', views.contacto),
]