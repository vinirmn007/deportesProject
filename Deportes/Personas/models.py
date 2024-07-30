from django.db import models

# Create your models here.
class Persona(models.Model):
    class meta:
        abstract = True
    
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=11)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()
    celular = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre + ' ' + self.dni
    
class Juez(Persona):
    idJuez = models.CharField(max_length=10, primary_key=True)

class Entrenador(Persona):
    preparacion = models.CharField(max_length=50)

class Deportista(Persona):
    golesAnotados = models.IntegerField()
    categoria = models.CharField(max_length=50)