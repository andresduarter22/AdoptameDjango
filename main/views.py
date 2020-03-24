from django.shortcuts import render
from .models import User, Animal, Form, PhoneNumber
from django.http import HttpResponse

def home(response):
    return render(response, "main/home.html")

def homeLog(response):
    return render(response, "main/homeLog.html")

def profile(response):
    return render(response, "main/profile.html")

def search(response):
    return render(response, "main/search.html")