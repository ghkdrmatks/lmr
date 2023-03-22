from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


