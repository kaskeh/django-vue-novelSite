from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import MyTokenSerializer, RegisterSerializer
from .models import User

# Create your views here.

##  不需要携带token就能访问接口
def ListShops(requests):
    return HttpResponse("this is shop list")

# 带有权限认证的视图
class DetailsView(APIView):

    # 会覆盖setting.py中设置的，等于是这里设置的优先级高
    permission_classes = [permissions.IsAuthenticated]   # 权限过滤，通过的返回True
    authentication_classes = (authentication.JWTAuthentication,)   # 认证过滤

    def get(self, request, *args, **kwargs):
        print('authenticate: ', request.successful_authenticator.authenticate(request))
        print('token信息: ', request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request))))
        print('登录用户: ', request.successful_authenticator.get_user(request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request)))))
        return Response('get ok')

    def post(self, request, *args, **kwargs):
        return Response('post ok')

# 自定义的登陆视图
class LoginView(TokenViewBase):
    serializer_class = MyTokenSerializer  # 使用刚刚编写的序列化类

    # post方法对应post请求，登陆时post请求在这里处理
    def post(self, request, *args, **kwargs):
        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'验证失败： {e}')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# 自定义注册视图
class RegisterView(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = RegisterSerializer

# 自定义验证登录后台
class myBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # 可以通过三种方式进行登录，用户账号，用户邮箱，用户手机号码
            user = User.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None