from django.db import models

# Create your models here.
## nombre Usuario -> es la persona que se loguea

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=40)
    correo = models.EmailField(max_length=50)
    nombre_usuario =  models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)

    def __str__(self):
        return "Nombre: "+self.nombre + " Usuario: "+self.nombre_usuario

class Mascota (models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10,choices=(('Macho','Macho'),('Hembra','Hembra')))
    edad = models.IntegerField()
    descripcion = models.TextField(max_length=300)
    tamanio = models.CharField(max_length=15, verbose_name='Tamaño')
    foto = models.ImageField(max_length=60)
    raza = models.CharField(max_length=30) 
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre: "+self.nombre 

class Perdido (models.Model):
    fecha_perdido = models.DateField()
    valido_hasta = models.DateField()
    siencontrado = models.BooleanField()
    fecha_encontrado = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
