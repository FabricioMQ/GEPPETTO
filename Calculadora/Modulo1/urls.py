from django.urls import path
from .views import *

urlpatterns = [
    path('cbase/',ConverView,name='Modulo1_api')
]