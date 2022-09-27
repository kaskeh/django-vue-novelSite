from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import status
from rest_framework import permissions
##
from .serializers import MyTokenSerializer


# Create your views here.

##  不需要携带token就能访问接口
def ListShops(requests):
    return HttpResponse("this is shop list")


class DetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)

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
