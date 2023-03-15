from rest_framework.serializers import ModelSerializer
from .models import *

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
