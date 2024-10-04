from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.ApiLibros.models import Libros
from apps.ApiLibros.api.serializers import LibrosSerializers

class LibrosAPIVew(APIView):
    def get(self, request):
        serializer = LibrosSerializers(Libros.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request):
        serializer = LibrosSerializers(data=request.data)
        serializer.is_valid (raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

