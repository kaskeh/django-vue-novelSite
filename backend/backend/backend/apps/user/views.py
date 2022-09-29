import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from django_redis import get_redis_connection

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
from .utils import get_user_by_account

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

# 验证号码是否唯一, 由于是不需要使用序列化器，故继承最基础的APIView视图类
class check_mobile(APIView):

    def get(self, request, mobile):
        ret = get_user_by_account(mobile)
        if ret is not None:
            return Response({"message": "手机号已经被注册了！"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "手机号未被注册！"})

from backend.settings import constants
from backend.uitls.EMS import sendEmail

class emailCodeAPIView(APIView):
    def get(self, request, email):
        """ 邮箱验证码发送 """

        # # 1. 判断邮箱是否在60秒内曾经发送过验证码
        redis_conn = get_redis_connection("verify_codes")
        ret = redis_conn.get("email_%s" % email)
        if ret is not None:
            return Response({"message": "验证码60秒内已经发生过，请耐心等待"})

        # 2. 生成验证码
        sms_code = "%06d" % random.randint(1, 999999)

        # 3. 保存验证码到redis
        redis_conn.setex("sms_%s" % email, constants.EMS_EXPIRE_TIME, sms_code)
        redis_conn.setex("email_%s" % email, constants.SMS_INTERVAL_TIME, "_")

        # 4. 调用发送邮件组件，发送验证码
        try:
            sendEmail.sendMailCode(message="您正在申请发送验证码：为了账号安全，请在指定位置输入下列验证码：{} 。 验证码涉及个人账号隐私安全，切勿向他人透漏。".format(sms_code)
                           ,Subject="可容书阁验证码邮件"
                           ,sender_show="可容书阁"
                           ,recipient_show=email
                           ,to_addrs=email)
        except:
            return Response({"message": "发送验证码失败"})

        # 5. 响应发送验证码的结构
        return Response({"message": "发送验证码成功！"})
