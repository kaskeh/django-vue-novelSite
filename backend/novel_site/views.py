from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
import json
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
    if request.method == "POST":
        # 查看当前用户账号是否有重复的
        print("userName", request.POST)
        print("request.body", request.body)

        return HttpResponse("post请求")
    return HttpResponse("hahaha")

def token(request):
    token = get_token(request)
    result = {"resCode": 0,'token': token}
    # return JsonResponse()
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")