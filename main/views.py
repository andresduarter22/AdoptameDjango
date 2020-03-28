from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import User, Animal, Form, PhoneNumber
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login


class Home(View):
    def get(self, request):
        return render(request, "main/index.html")

    def post(self, request):
        data = request.POST
        if 'Register' in data:
            self.createUser(data)
            return render(request, "main/index.html")
        elif 'Inicio' in data:
            user = authenticate(username=str(data.get("UserName")), password=str(data.get("UserPsswd")))
            # with open('./log.txt', 'w') as f:
            #   f.write(str(user))
            do_login(request, user)
            return redirect('/homeLog')

    def createUser(self, data):
        user = User.objects.create_user(str(data.get("SPName")), str(data.get("SPEmail")), str(data.get("SPPssw")))
        user.save()


def homeLog(response):
    return render(response, "main/homeLog.html")


def profile(response):
    return render(response, "main/profile.html")


def search(response):
    return render(response, "main/search.html")


def logout(response):
    do_logout(response)
    return redirect("/")
