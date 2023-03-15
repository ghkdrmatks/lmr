from django.urls import path
from . import views

urlpatterns = [
    path('get/Restaurant', views.getRestaurant, name="getRestaurant"),
]
