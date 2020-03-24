from django.shortcuts import render
from .models import User, Animal, Form, PhoneNumber
from django.http import HttpResponse

def home(respone):
    return render(respone, "main/home.html")

def homeLog(respone):
    return render(respone, "main/homeLog.html")

def profile(respone):
    return render(respone, "main/profile.html")

def search(respone):
    return render(respone, "main/search.html")