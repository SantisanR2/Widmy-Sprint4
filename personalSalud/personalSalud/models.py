from django.db import models

# Model: personalSalud
# Fields: id, nombre, apellido, edad, sexo, especialidad
# Description: Modelo que representa el personal de salud
class PersonalSalud(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre 
