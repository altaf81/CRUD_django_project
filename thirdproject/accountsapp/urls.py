from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', my_login, name="login"),
    path('logout/', my_logout, name="logout"),
    path('register/', register, name="register")

]
