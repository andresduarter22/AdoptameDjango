from django.shortcuts import render
from django.http import HttpResponse

def home(respone):
    return HttpResponse("<h1>Hello world</h1>")
