from django.urls import path

from . import views

urlpatterns =[
    path("", views.Home.as_view(), name="index"),
    path("home/", views.Home.as_view(), name="home"),
    path("homeLog/", views.homeLog, name="homeLog"),
    path("profile/", views.profile, name="profile"),
    path("search/", views.search, name="search")
]
