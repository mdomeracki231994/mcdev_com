from django.urls import path
from . import views


urlpatterns =  [
    path('customer_admin/', views.say_hello)
]