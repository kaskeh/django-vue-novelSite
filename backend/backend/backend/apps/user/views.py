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

##  ����ҪЯ��token���ܷ��ʽӿ�
def ListShops(requests):
    return HttpResponse("this is shop list")

# ����Ȩ����֤����ͼ
class DetailsView(APIView):

    # �Ḳ��setting.py�����õģ��������������õ����ȼ���
    permission_classes = [permissions.IsAuthenticated]   # Ȩ�޹��ˣ�ͨ���ķ���True
    authentication_classes = (authentication.JWTAuthentication,)   # ��֤����

    def get(self, request, *args, **kwargs):
        print('authenticate: ', request.successful_authenticator.authenticate(request))
        print('token��Ϣ: ', request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request))))
        print('��¼�û�: ', request.successful_authenticator.get_user(request.successful_authenticator.get_validated_token(
            request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request)))))
        return Response('get ok')

    def post(self, request, *args, **kwargs):
        return Response('post ok')

# �Զ���ĵ�½��ͼ
class LoginView(TokenViewBase):
    serializer_class = MyTokenSerializer  # ʹ�øոձ�д�����л���

    # post������Ӧpost���󣬵�½ʱpost���������ﴦ��
    def post(self, request, *args, **kwargs):
        # ʹ�øոձ�дʱ���л������½��֤��������Ӧ
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'��֤ʧ�ܣ� {e}')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# �Զ���ע����ͼ
class RegisterView(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = RegisterSerializer

# �Զ�����֤��¼��̨
class myBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # ����ͨ�����ַ�ʽ���е�¼���û��˺ţ��û����䣬�û��ֻ�����
            user = User.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# ��֤�����Ƿ�Ψһ, �����ǲ���Ҫʹ�����л������ʼ̳��������APIView��ͼ��
class check_mobile(APIView):

    def get(self, request, mobile):
        ret = get_user_by_account(mobile)
        if ret is not None:
            return Response({"message": "�ֻ����Ѿ���ע���ˣ�"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "�ֻ���δ��ע�ᣡ"})

from backend.settings import constants
from backend.uitls.EMS import sendEmail

class emailCodeAPIView(APIView):
    def get(self, request, email):
        """ ������֤�뷢�� """

        # # 1. �ж������Ƿ���60�����������͹���֤��
        redis_conn = get_redis_connection("verify_codes")
        ret = redis_conn.get("email_%s" % email)
        if ret is not None:
            return Response({"message": "��֤��60�����Ѿ��������������ĵȴ�"})

        # 2. ������֤��
        sms_code = "%06d" % random.randint(1, 999999)

        # 3. ������֤�뵽redis
        redis_conn.setex("sms_%s" % email, constants.EMS_EXPIRE_TIME, sms_code)
        redis_conn.setex("email_%s" % email, constants.SMS_INTERVAL_TIME, "_")

        # 4. ���÷����ʼ������������֤��
        try:
            sendEmail.sendMailCode(message="���������뷢����֤�룺Ϊ���˺Ű�ȫ������ָ��λ������������֤�룺{} �� ��֤���漰�����˺���˽��ȫ������������͸©��".format(sms_code)
                           ,Subject="���������֤���ʼ�"
                           ,sender_show="�������"
                           ,recipient_show=email
                           ,to_addrs=email)
        except:
            return Response({"message": "������֤��ʧ��"})

        # 5. ��Ӧ������֤��Ľṹ
        return Response({"message": "������֤��ɹ���"})
