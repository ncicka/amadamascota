from django.db import models

# Create your models here.
## nombre Usuario -> es la persona que se loguea

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=40)
    correo = models.CharField(max_length=50)


class Mascota (models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField(max_length=2)
    descripcion = models.TextField(max_length=300)
    tamanio = models.CharField(max_length=15)
    foto = models.CharField(max_length=60)
    raza = models.CharField(max_length=30) 
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Perdido (models.Model):
    fecha_perdido = models.DateField()
    valido_hasta = models.DateField()
    siencontrado = models.BooleanField()
    fecha_encontrado = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
