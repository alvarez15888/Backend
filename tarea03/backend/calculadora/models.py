from django.db import models


class Material(models.Model):
    nombre = models.CharField(max_length=100)
    masa = models.FloatField(help_text="Masa del material en kg")

    def __str__(self):
        return self.nombre

class Energia(models.Model):
    valor = models.FloatField(help_text="Energía en Joules")

    def __str__(self):
        return f"{self.valor} J"

class Calculo(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    energia = models.ForeignKey(Energia, on_delete=models.CASCADE)
    fecha_calculo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Material: {self.material.nombre}, Energía: {self.energia.valor} J"
    
    @property
    def c(self):
        return self.energia/self.material