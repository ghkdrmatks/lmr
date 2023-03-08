from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.getUser, name="user"),
    path('menu/', views.getMenu, name="menu"),
]
