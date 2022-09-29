from django.contrib import admin
from django.urls import path, re_path,include
# 只改变了请求token返回的，刷新token依旧保持不动
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import LoginView, RegisterView, DetailsView, check_mobile
# from django.contrib.auth import login, logout

urlpatterns = [
    path(r'login/', LoginView.as_view()),
    path(r'register/', RegisterView.as_view()),
    path(r'DetailsView/', DetailsView.as_view()),
    re_path(r'check_mobile/(?P<mobile>1[3-9]\d{9})/', check_mobile.as_view()),

]