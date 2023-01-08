from django.db import models

# Create your models here.

class Docente(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    Apellido_Paterno=models.CharField(max_length=20)
    Apellido_Materno=models.CharField(max_length=20)
    DNI=models.CharField(max_length=8)
    Fecha_Nacimiento=models.DateField()
    Fecha_Registro=models.DateTimeField(auto_now_add=True)
    Estado=models.CharField(max_length=15)