from django.db import models


class ayuda(models.Model)

class producto(models.Model):

    id_producto = models.CharField(primary_key=True, max_length=6)
    nombre_producto = models.CharField(max_length=50)
    marca_producto = models.CharField(max_length=20)
    cantidad_necesaria_prod = models.CharField(max_length=2)
    valor_producto = models.CharField(max_length=5)

    def __str__(self):
        return str(self.nombre_producto)+""+str(self.marca_producto)
