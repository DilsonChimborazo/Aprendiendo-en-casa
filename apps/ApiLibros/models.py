from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo=models.CharField(max_length=100)
    autor=models.CharField(max_length=100)
    fecha_publicacion=models.DateField(max_length=100)
def __str__(self):
    return self.titulo

