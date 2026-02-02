from django.contrib import admin
from .models import Entrada


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'creado')
	search_fields = ('titulo', 'contenido')

from .models import Ingreso, Salida


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
	list_display = ('monto', 'descripcion', 'creado', 'modificado')
	search_fields = ('descripcion',)
	list_filter = ('creado',)


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
	list_display = ('monto', 'descripcion', 'creado', 'modificado')
	search_fields = ('descripcion',)
	list_filter = ('creado',)
