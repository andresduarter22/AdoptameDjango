from django.db import models

# Create your models here.

class Usuario(models.Model):
    ID
    nombre = models.CharField(max_length=200)
    correo

    def __str__(self):
        return self.name
class Formulario(models.Model):
    ID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ID_animal
    fecha
    zona
    celular
class Animal(models.Model):
    ID_animal
    raza
    sexo
    tamanio
    edad
    foto
    estado
class Telefono(models.Model):
    ID
    celular
