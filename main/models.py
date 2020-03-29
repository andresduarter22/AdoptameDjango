from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    ID_user = models.AutoField(unique=True, primary_key=True)
    UserName = models.CharField(max_length=200, default="Pedro")
    Name = models.CharField(max_length=200)
    ProfilePic = models.ImageField(default="main/static/media/user/rey.png", upload_to="main/static/media/user/")

class Animal(models.Model):
    STATUS_CHOICES = (
        ('a', 'for_adoption'),
        ('f', 'found'),
        ('l', 'lost'),
    )
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )
    SIZE_CHOICES = (
        ('s', 'short'),
        ('m', 'medium'),
        ('b', 'big')
    )
    RACE_CHOICES = (
        ('d', 'dog'),
        ('c', 'cat'),
        ('o', 'other')
    )
    ID_animal = models.AutoField(unique=True, primary_key=True)
    picture = models.ImageField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    race = models.CharField(max_length=200, choices=RACE_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    size = models.CharField(max_length=200, choices=SIZE_CHOICES)
    

class Form(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    Date = models.DateField()
    Area = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)

class PhoneNumber(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cellphone = models.CharField(max_length=10)
