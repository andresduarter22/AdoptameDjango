from datetime import date

from django.shortcuts import render, redirect
from django.views import View
from .models import User as UserDB, Animal, Form as FormDB, PhoneNumber
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

            if user:
                do_login(request, user)
                return redirect('/homeLog')
            else:
                return redirect('/')

    def createUser(self, data):
        user = User.objects.create_user(str(data.get("SPName")), str(data.get("SPEmail")), str(data.get("SPPssw")))
        user.save()
        usr = UserDB(None, str(user.username), str(data.get("SPFisrtName") + " " + data.get("SPLastName")), None)
        UserDB.save(usr)

def form(request):
    data = request.POST

    # Añadir animal
    animal = Animal(ID_animal=None, picture=request.FILES["PetImage"], status=str(data.get("inputEstado")), race=str(data.get("inputEspecie")), gender=str(data.get("inputSexo")), size=str(data.get("inputT")))
    animal.save()
    # Añadir numero de telefono
    q = UserDB.objects.filter(UserName=request.user.username)
    cell = PhoneNumber(ID_user=q[0], cellphone=str(data.get("FormCellPhone")))
    PhoneNumber.save(cell)
    # Añadir a form
    f = FormDB(ID_user=q[0], ID_animal=Animal.objects.latest("ID_animal"), Date=date.today(), Area=str(data.get("Place")))
    FormDB.save(f)
    return redirect("/homeLog/")


def homeLog(response):
    # data = User.objects.get(id=response.user.id)
    usr = {"user_info": response.user.id, "name": UserDB.Name, "userName": UserDB.UserName, "picture": UserDB.ProfilePic}
    return render(response, "main/homeLog.html", usr)


def profile(response):
    q = UserDB.objects.filter(UserName= response.user.username)
    q1 = FormDB.objects.filter(ID_user=q.values('ID_user')[0]['ID_user'])
    tel = PhoneNumber.objects.filter(ID_user=q.values('ID_user')[0]['ID_user'])
    an = Animal.objects.filter(ID_animal=q1.values('ID_animal')[0]['ID_animal'])
    usr = {"ID": response.user.id, "name": str(q.values('Name')[0]['Name']), "userName":  str(q.values('UserName')[0]['UserName']),
           "picture": UserDB.ProfilePic, "email": response.user.email, "cellPhone": str([x['cellphone'] for x in list(tel.values('cellphone'))]).translate(str.maketrans('', '', '[\']')),
           "Publicaciones": q1, "animal": an.values('description')[0]['description'], "user": q}


    return render(response, "main/profile.html", usr)


def search(request):
    data = request.POST
    q1 = Animal.objects.all()
    q2 = FormDB.objects.all()
    q3 = PhoneNumber.objects.all()

    def test(n):
        return "hola" + str(n)
    q = Animal.objects.filter(status=str(data.get("inputEstadoS"))).filter(race=str(data.get("inputEspecieS"))).filter(gender=str(data.get("inputSexoS"))).filter(size=str(data.get("inputTS")))
    # with open('./log.txt', 'w') as f:
    #    f.write(str(q))
    if not q:
        d1 = {"busqueda": q1, "form": q2, "phone": q3, "test": test}
        return render(request, "main/search.html", d1)
    else:
        d = {"busqueda": q}
        return render(request, "main/search.html", d)


def logout(response):
    do_logout(response)
    return redirect("/")

def changeUserPic(response):
    user = UserDB.objects.filter(UserName= response.user.username)[0]
    user.ProfilePic = response.FILES["UserImage"]
    user.save()
    return redirect("/profile/")
