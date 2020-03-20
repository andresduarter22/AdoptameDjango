from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    ID_user = models.IntegerField(unique=True, primary_key=True)
    Name = models.CharField(max_length=200)
    Mail = models.EmailField(max_length = 254)
    password = forms.CharField(widget=forms.PasswordInput)
    def __str__(self):
        return self.nombre


class Form(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    Date =
    Area =
    cellphone = models.CharField(max_length=200)


class Animal(models.Model):
    STATUS_CHOICES = (
        ('a', 'for_adoption'),
        ('f', 'found'),
        ('l', 'lost'),
    )
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f','female')
    )
    ID_animal = models.IntegerField(unique=True, primary_key=True)
    race = models.CharField(max_length=200)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    size =
    age = models.IntegerField()
    picture = models.ImageField()
    status = models.CharField(max_length=200,choices=STATUS_CHOICES)


class PhoneNumber(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cellphone = models.CharField(max_length=10)
