from django.shortcuts import render, redirect
from django.views import View
from .models import User as UserDB, Animal, Form, PhoneNumber
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User


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
        usr = UserDB(None, str(user.username), str(data.get("SPFisrtName") + " " + data.get("SPLastName")), None)
        UserDB.save(usr)



def homeLog(response):
    # data = User.objects.get(id=response.user.id)
    usr = {"user_info": response.user.id, "name": UserDB.Name, "userName": UserDB.UserName, "picture": UserDB.ProfilePic}
    return render(response, "main/homeLog.html", usr)


def profile(response):
    # q = User.objects.raw('SELECT  * FROM User ')
    usr = {"ID": response.user.id, "name": UserDB.Name, "userName": UserDB.UserName, "picture": UserDB.ProfilePic, "email": User.email}
    return render(response, "main/profile.html", usr)


def search(response):
    return render(response, "main/search.html")


def logout(response):
    do_logout(response)
    return redirect("/")
