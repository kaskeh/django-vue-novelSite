from django.shortcuts import render
from django.http import HttpResponse
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