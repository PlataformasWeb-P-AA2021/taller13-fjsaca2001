from django.db import models


# Create your models here.

class Edificio(models.Model):
    class Meta:
        verbose_name_plural = "Edificios"

    opciones_tipo = (
        ('recidencial', 'Edificio Recidencial'),
        ('comercial', 'Edificio Comercial'),
    )
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50, choices=opciones_tipo)

    def __str__(self):
        return "%s - %s - %s - %s" % (
            self.nombre,
            self.direccion,
            self.ciudad,
            self.tipo
        )

    def obtenerNroCuartos(self):
        valor = [d.numeroCuartos for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtenerCostoTotal(self):
        valor = [d.costoDepartamento for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

class Departamento(models.Model):
    class Meta:
        verbose_name_plural = "Departamentos"

    nombrePropietario = models.CharField(max_length=100)
    costoDepartamento = models.DecimalField(max_digits=10000, decimal_places=2)
    numeroCuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name="departamentos")

    def __str__(self):
        return "%s - %f - %d" % (
            self.nombrePropietario,
            self.costoDepartamento,
            self.numeroCuartos
        )
