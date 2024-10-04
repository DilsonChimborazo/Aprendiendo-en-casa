from rest_framework.serializers import ModelSerializer
from apps.PrimeraApi.models import Usuarios

class UsuariosSerializers(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'