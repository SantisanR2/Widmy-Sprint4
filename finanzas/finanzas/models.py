from django.db import models

class factura(models.Model):
    fecha = models.DateField()
    ciudad = models.CharField(max_length=50)
    servicio = models.CharField(max_length=50)
    facturacion = models.IntegerField()

    def __str__(self):
        return self.id_factura
