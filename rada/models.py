from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=255)
    puerto = models.IntegerField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)
