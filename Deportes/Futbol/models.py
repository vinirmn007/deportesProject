from django.db import models
from Personas.models import *

# Create your models here.
class TipoTorneo(models.TextChoices):
    LIGA = 'LIGA', 'Liga'
    LIGUILLA = 'LIGUILLA', 'Liguilla'
    EXHIBICION = 'EXHIBICION', 'Exhibicion'
    PLAY_OFF = 'PLAY_OFF', 'Play Off'
    SUIZO = 'SUIZO', 'Suizo'
    OTRO = 'OTRO', 'Otro'

class Regla(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    class Meta:
        abstract = True

    nombreDeporte = models.CharField(max_length=50)
    N_PARTICIPANTES = 11

    reglaList = models.ManyToManyField(Regla)

class Futbol(Deporte):
    pass

class Equipo(models.Model):
    idEquipo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    escudo = models.URLField(default="https://upload.wikimedia.org/wikipedia/commons/8/8d/Escudo_de_la_Federaci%C3%B3n_Ecuatoriana_de_F%C3%BAtbol_2019.jpg", max_length=200)
    color = models.CharField(max_length=50)
    puntosConseguidos = models.IntegerField()

    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    deportistaList = models.ManyToManyField(Deportista)

    def deportistasMax(self):
        if self.deportistaList.count() > 11:
            return "Máximo de deportistas alcanzado"

    def __str__(self):
        return self.nombre

class Eventos(models.TextChoices):
    SANCION = 'SANCION', 'Sanción'
    GOL = 'GOL', 'Gol'
    CAMBIO = 'CAMBIO', 'Cambio'
    LESION = 'LESION', 'Lesión'
    PENAL = 'PENAL', 'Penal'
    FUERA_JUEGO = 'FUERA_JUEGO', 'Fuera de Juego'
    OTRO = 'OTRO', 'Otro'

class Inscripcion(models.Model):
    fechaInscripcion = models.DateField()

    equiposInscritos = models.ManyToManyField(Equipo)

    def ordenar(self):
        pass
    
    def __str__(self):
        return str(self.fechaInscripcion)

class Encuentro(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    puntuacionEquipo1 = models.IntegerField()
    puntuacionEquipo2 = models.IntegerField()
    resultado = models.CharField(max_length=50, blank=True)

    equipo1 = models.ForeignKey(Equipo, related_name='equipo1', on_delete=models.CASCADE)
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2', on_delete=models.CASCADE)
    eventoList = models.CharField(max_length=50, choices=Eventos.choices)

    def definirResultado(self):
        if self.puntuacionEquipo1 > self.puntuacionEquipo2:
            self.resultado = f"Gana {self.equipo1}"
        elif self.puntuacionEquipo1 < self.puntuacionEquipo2:
            self.resultado = f"Gana {self.equipo2}"
        else:
            self.resultado = 'Empate'
    
    def save(self, *args, **kwargs):
        self.definirResultado()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.equipo1} vs {self.equipo2} - {self.resultado}"

class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    categoria = models.CharField(max_length=50)
    maxParticipantes = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=TipoTorneo.choices)

    campeon = models.ForeignKey(Equipo, related_name='campeon', on_delete=models.CASCADE, null=True, blank=True)
    subcampeon = models.ForeignKey(Equipo, related_name='subcampeon', on_delete=models.CASCADE, null=True, blank=True)
    juezList = models.ManyToManyField(Juez)
    equipoList = models.ManyToManyField(Equipo)
    encuentroList = models.ManyToManyField(Encuentro)
    
    def __str__(self):
        return self.nombre
    
class TablaPosiciones(models.Model):
    posicionList = models.ManyToManyField(Equipo)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def ordenar(self):
        pass