from django.urls import path

from . import views

urlpatterns =[
    path("home/", views.home, name="home"),
    path("homeLog/", views.homeLog, name="homeLog"),
    path("profile/", views.profile, name="profile"),
    path("search/", views.search, name="search")
]
