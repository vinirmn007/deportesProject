from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Torneo)
admin.site.register(Regla)
admin.site.register(Equipo)
admin.site.register(Encuentro)
admin.site.register(TablaPosiciones)
admin.site.register(Inscripcion)

