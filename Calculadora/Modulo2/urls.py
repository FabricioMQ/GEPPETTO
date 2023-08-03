from django.urls import path
from .views import *
urlpatterns = [
    path('numbes/',numbes,name='Modulo2_api')
]