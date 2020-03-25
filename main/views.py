from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import User, Animal, Form, PhoneNumber
from django.http import HttpResponse,HttpRequest



class Home(View):
    def get(self, request):
        return render(request, "main/index.html")

    def post(self, request):
        self.createUser(request.POST)
        #with open('./log.txt', 'w') as f:
        #    f.write(str(request.POST))
        return render(request, "main/index.html")

    def createUser(self, data):
        user = User(Name=str(data.get("SPName")), Mail=str(data.get("SPEmail")))
        user.save()



def homeLog(response):
    return render(response, "main/homeLog.html")

def profile(response):
    return render(response, "main/profile.html")

def search(response):
    return render(response, "main/search.html")