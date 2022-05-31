from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('construction/', construction, name='construction'),
    path('restaurant/', restaurant, name='restaurant'),
    path('mechanics/', mechanics, name='mechanics'),
]