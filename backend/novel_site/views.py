from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
import json
from .models import User

from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer


# Create your views here.

def books_cates(request):
    resData = {
        "resCode": 0, # 非0即错误
        "data": [
            {"id": 0, "text": "首页", "url": "/"},
            {"id": 1, "text": "玄幻", 'url': '/xuanhuan'},
            {"id": 2, "text": "修真", 'url': '/xiuzhen'},
            {'id': 3, 'text': '都市', 'url': '/dushi'},
            {'id': 4, 'text': '历史', 'url': '/lishi'},
            {'id': 5, 'text': '网游', 'url': '/wangyou'},
            {'id': 6, 'text': '科幻', 'url': '/kehuan'},
            {'id': 7, 'text': '言情', 'url': '/yanqing'},
            {'id': 8, 'text': '其他', 'url': '/qita'},
            {'id': 8, 'text': '完本', 'url': '/wanben'}
        ],
        'message': '主页小说分类'
    }
    # return HttpResponse("over", status=200)
    return HttpResponse(json.dumps(resData))

def accounts(request, id):
    return render(request, 'login.html')

# 如果登录成功，设置cookie
def login(request):
    return HttpResponse("哈哈哈")

    # resData = {
    #     "resData": 0,  # 0为验证成功，1为验证失败
    #     "message": "用户验证成功，将跳转到用户中心页面"
    # }
    #
    # # 检查是否以post的方式发起的请求
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = User.objects.filter(username__exact=username, password__exact=password)
    #         if user:
    #             resData["resData"] = 0
    #             resData["message"] = "用户验证成功，将跳转到用户中心页面"
    #
    #             # 将username写入浏览器cookie,有效时间为360秒
    #             response.set_cookie('username', username, 360)
    #             return HttpResponse(json.dumps(resData))
    #         else:
    #             resData["resData"] = 1
    #             resData["message"] = "用户帐号或密码不正确，请重试"
    #             return HttpResponse(json.dumps(resData))
    #
    # else:
    #     resData["resData"] = 2
    #     resData["message"] = "请求不合规范"
    #     return HttpResponse(json.dumps(resData))

def register(request):
    """
        registerCode: 0(用户已存在，前端提示用户更换要注册的用户名)
                      1(用户注册成功，然后让前端跳转登录)
                      2(注册失败)
    """
    if request.method == "POST":

        # 用提交的数据生成表单

        # 反序列化
        registerInfo = json.loads(request.body)
        # 查看当前用户账号是否有重复的
        try:
            username_db = User.objects.get(username=registerInfo["username"])
            return JsonResponse({"resCode": 0,
                                 "mes": "当前注册的用户名已存在",
                                 "registerCode": 0})
        except Exception as e:
            print("当前注册的用户名不存在")
            # 生成用户数据进入表里
            userInfo = User(
                username = registerInfo["username"],
                email = registerInfo["mail"]
            )
            # 不可使用 password = registerInfo["password"]的方式直接赋值
            # 要使用set_password（）的辅助方法对明文密码哈希索引加密
            userInfo.set_password(str(registerInfo["password"]))
            userInfo.save()
        return JsonResponse({"resCode":0,
                             "mes":"当前注册的用户名不存在,已完成注册",
                             "registerCode": 1})
    return JsonResponse({"resCode": 0, "mes": None})

def token(request):
    token = get_token(request)
    result = {"resCode": 0,'token': token}
    # return JsonResponse()
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")

# 指定它的序列化器为我们自定义的序列化器MyTokenObtainPairSerializer
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LoginView(APIView):
    def get(self, request):   #         # 请求为get时的业务逻辑
        """业务逻辑"""
        print("haha")
        return HttpResponse("认证通过，get")

    def post(self, request): # 请求为post时的业务逻辑
        """业务逻辑"""

        #获取前端提交的用户名
        account = request.data.get("username")
        # 获取前端提交的密码
        password = request.data.get("password")
        return HttpResponse("认证通过，post")

class RegisterView(APIView):
    def get(self, request):   #         # 请求为get时的业务逻辑
        """业务逻辑"""
        print("haha")
        return HttpResponse("认证通过，get")

    def post(self, request): # 请求为post时的业务逻辑
        """业务逻辑"""

        username = request.data.get("username")
        passwd = request.data.get("password")
        email = request.data.get("mail")

        # 如果用户名存在则响应客户端用户名已存在，获取用户名 模型类.objects.filter(条件)
        if User.objects.filter(username=username):
            return Response({"code": 407, "msg": "用户名已被注册"})
        try:
            User.objects.create(username=username, password=passwd, email=email)
        except Exception as e:
            print("注册出现问题", e)
            return Response({"code": 405, "msg": "注册失败"})

        return Response({"code": 200, "msg": "注册成功"})

# @csrf_exempt  # 屏蔽跨域检测，不进行csrf保护
# @csrf_protect 是 开启csrf验证的装饰器
def userTest(request):
    print(request.body)

    return HttpResponse("111")

def userTest2(request):
    print(request.body)

    return HttpResponse("222")