from django.urls import path
from . import views

urlpatterns = [
    path('restaurant', views.getRestaurant, name="getRestaurant"),
    path('menu/<int:restaurant>', views.getMenuByRestaurant, name="getMenubyRestaurant"),
    path('menu', views.getMenu, name="getMenu"),
]
