from rest_framework.serializers import ModelSerializer
from apps.ApiLibros.models import Libros

class LibrosSerializers(ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'