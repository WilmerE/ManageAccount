from django.db import models


class Entrada(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField(blank=True)
	creado = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Entrada'
		verbose_name_plural = 'Entradas'

	def __str__(self):
		return self.titulo


class Ingreso(models.Model):
	monto = models.DecimalField(max_digits=12, decimal_places=2)
	descripcion = models.CharField(max_length=255, blank=True)
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Ingreso'
		verbose_name_plural = 'Ingresos'

	def __str__(self):
		return f"{self.monto:,.2f} - {self.descripcion} - {self.creado.date()}"


class Salida(models.Model):
	monto = models.DecimalField(max_digits=12, decimal_places=2)
	descripcion = models.CharField(max_length=255, blank=True)
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Salida'
		verbose_name_plural = 'Salidas'

	def __str__(self):
		# Formatea con signo y separador de miles: e.g. -5,000.00 - descripcion - 2026-01-29
		try:
			return f"{self.monto:+,.2f} - {self.descripcion} - {self.creado.date()}"
		except Exception:
			return f"{self.monto} - {self.descripcion} - {self.creado.date()}"
