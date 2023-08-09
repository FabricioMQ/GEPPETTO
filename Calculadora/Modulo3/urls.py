from django.urls import path
from .views import *
urlpatterns = [
    path('problemasAI/',problemasAI,name='Modulo3_api')
]