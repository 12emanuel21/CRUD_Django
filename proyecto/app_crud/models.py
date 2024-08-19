from django.db import models

# Create your models here.

generos = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
)


class Empleado(models.Model):
    Nombre = models.CharField(max_length=150)
    Apellido = models.CharField(max_length=150)
    Email = models.EmailField(max_length=150)
    Edad = models.IntegerField()
    Generos = models.CharField(max_length=100, choices=generos)
    Salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Fecha_inicial = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Fecha_actualizada = models.DateTimeField(auto_now_add=False, auto_now=True)


    
    class Meta:
        db_table = "empleados"
        ordering = ['-Fecha_inicial']


