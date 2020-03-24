from django.shortcuts import render
from .models import User, Animal, Form, PhoneNumber
from django.http import HttpResponse

def home(respone):
    return render(respone,"main/index.html")
