from django.urls import path, include
# from django.contrib.auth import login, logout
from . import views

urlpatterns = [
    path('navBar/', views.navBar),
]