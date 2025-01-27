from django.db import models

# Create your models here.
class Mecanico (models.Model):
    ci = models.CharField(max_length=11 , primary_key=True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Carro(models.Model):
     matricula = models.CharField(max_length=7, primary_key=True)
     marca = models.CharField(max_length = 100)
     modelo = models.CharField(max_length = 100)
     ci_mecanico = models.ForeignKey(Mecanico,on_delete=models.CASCADE)
     
     def __str__(self):
         return f"{self.marca} {self.modelo}"
     
class Propietario (models.Model):
    ci = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    carros = models.ManyToManyField(Carro,related_name='carros')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"