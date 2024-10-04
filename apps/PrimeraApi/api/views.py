from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.PrimeraApi.models import Usuarios
from apps.PrimeraApi.api.serializers import UsuariosSerializers

class UsuariosAPIView(APIView):
    def get(self, request):
        serializer = UsuariosSerializers(Usuarios.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (status=status.HTTP_200_OK, data=serializer.data)
        
