from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    
    def __srt__(self):
        return self.nombre
