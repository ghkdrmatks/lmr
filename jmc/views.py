from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

@api_view(['GET'])
def getUser(request):
    datas = User.objects.all()
    serializer = UserSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMenu(request):
    datas = Menu.objects.all()
    serializer = MenuSerializer(datas, many=True)
    return Response(serializer.data)
