from django.db import models


# Create your models here.

class User(models.Model):
    ID_user = models.AutoField(unique=True, primary_key=True)
    UserName = models.CharField(max_length=200, default="Pedro")
    Name = models.CharField(max_length=200)
    ProfilePic = models.FileField(default="user/rey.png", upload_to="user/")

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
    picture = models.FileField(default="animal/rey.png", upload_to="animal/")
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    race = models.CharField(max_length=200, choices=RACE_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    size = models.CharField(max_length=200, choices=SIZE_CHOICES)
    description = models.CharField(max_length=500, choices=SIZE_CHOICES, default="Description Example")
    

class Form(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    Date = models.DateField()
    Area = models.CharField(max_length=200)

class PhoneNumber(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cellphone = models.CharField(max_length=10)
