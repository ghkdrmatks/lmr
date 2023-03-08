from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
