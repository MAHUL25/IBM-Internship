from django.urls import path
from . import views

app_name = "credit_fraud"
urlpatterns = [
    path('', views.index, name="index"),
    path('formpage', views.Theform, name="Theform"),
    path('loginpage', views.LoginPage, name="loginPage"),
    path('registerpage', views.RegisterPage, name="registerPage")
]