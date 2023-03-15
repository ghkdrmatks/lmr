from django.urls import path
from . import views

urlpatterns = [
    path('get/restaurant', views.getRestaurant, name="getRestaurant"),
    path('get/menu/<int:restaurant>', views.getMenuByRestaurant, name="getMenubyRestaurant"),
    path('get/menu', views.getMenu, name="getMenu"),
]
