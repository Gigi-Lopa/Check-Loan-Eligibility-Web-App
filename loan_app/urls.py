from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/',views.mainPage, name="mainPage"),
    path("model/predict/", views.predictions),
    path("log/in/", views.logIn, name="logIn"),
    path("create/account/", views.renderCreateAccount, name="createAccount"),
    path("add/user/", views.addUsers, name="addUsers"),
    path("admin/admin123/", views.adminPage, name="adminPage"),
    path("auth/admin/", views.authAdmin, name= "authAdmin"),
    path("home/admin", views.homeAdmin, name="homeAdmin")
]