from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns =[
    path("", views.Home.as_view(), name="index"),
    path("home/", views.Home.as_view(), name="home"),
    path("homeLog/", login_required(views.homeLog), name="homeLog"),
    path("profile/", login_required(views.profile), name="profile"),
    path("search/", login_required(views.search), name="search"),
    path("logout/", views.logout, name = "logout")
]
