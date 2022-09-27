from django.contrib import admin
from django.urls import path, include
# 只改变了请求token返回的，刷新token依旧保持不动
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import LoginView
# from django.contrib.auth import login, logout

urlpatterns = [
    path(r'login/', LoginView.as_view()),

]