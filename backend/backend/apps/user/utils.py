from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import User

def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回的数据
    ：parms token 本次登录成功以后，返回jwt
    ：parms user 本次登录成功以后，从数据库中查询到的用户模型信息
    ：parms request 本次客户端的请求对象
    """
    return {
        'token': token,
        "id": user.id,
        "username": user.username
        # 'user': UserSerializer(user, context={'request': request}).data
    }

def get_user_by_account(account):
    """
    根据账号获取user对象
    ：parms account：账号，可以是用户名username，也可以是手机号mobile，或者是其他
    ：return： User对象 或者 None
    """
    try:
        user = User.objects.filter(Q(username=account)|Q(mobile=account)).first()
    except User.DoesNotExist:
        user = None
    else:
        return user