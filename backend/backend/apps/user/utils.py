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