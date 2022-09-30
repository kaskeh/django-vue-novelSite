from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import time, re

# 如果自定义了用户表，那么就要使用这个方法来获取用户模型
# 没有自定义的话可以使用以下方式加载用户模型:
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django_redis import get_redis_connection



# 不过这种是万能的
# User = get_user_model()


# 重写TokenObtainPairSerializer类的部分方法以实现自定义数据响应结构和payload内容
class MyTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        """
        此方法往token的有效负载 payload 里面添加数据
        例如自定义了用户表结构，可以在这里面添加用户邮箱，头像图片地址，性别，年龄等可以公开的信息
        这部分放在token里面是可以被解析的，所以不要放比较私密的信息
        :param user: 用戶信息
        :return: token
        """
        token = super().get_token(user)
        # 添加个人信息
        token['name'] = user.username
        return token

    def validate(self, attrs):
        """
        此方法为响应数据结构处理
        原有的响应数据结构无法满足需求，在这里重写结构如下：
        {
            "refresh": "xxxx.xxxxx.xxxxx",
            "access": "xxxx.xxxx.xxxx",
            "expire": Token有效期截止时间,
            "username": "用户名",
        }
        :param attrs: 請求參數
        :return: 响应数据
        """
        # data是个字典
        # 其结构为：{'refresh': '用于刷新token的令牌', 'access': '用于身份验证的Token值'}
        data = super().validate(attrs)

        # 获取Token对象
        refresh = self.get_token(self.user)
        # 加个token的键，值和access键一样
        data['token'] = data['access']
        # 然后把access键干掉
        del data['access']
        # 令牌到期时间
        timestamp = refresh.access_token.payload['exp']  # 有效期-时间戳
        time_local = time.localtime(int(timestamp))
        data['expire'] = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

        # 用户名
        data['username'] = self.user.username
        # 用户id
        data['userid'] = self.user.id

        return data

class RegisterSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    password2 = serializers.CharField(label='确认密码', write_only=True)
    sms_code = serializers.CharField(label='短信验证码', default=None, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'password2', 'sms_code', 'mobile', "email")
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 25,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 4,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    def validate_mobile(self, value):
        """验证手机号"""
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    def validate(self, attrs):
        # 判断两次密码
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('输入的两次密码不一致')

        # 查看提交过来的数据中是否有验证码
        if attrs["sms_code"] is not None:
            # 判断短信验证码
            redis_conn = get_redis_connection('verify_codes')
            # 获取真实验证码
            real_sms_code = redis_conn.get('sms_%s' % attrs['email'])
            # 如果取出来是None，那么代表已经超时了
            if real_sms_code is None:
                raise serializers.ValidationError('短信验证码无效')
            # 注意real_sms_code 从redis中取出来的是bytes类型，需要decode一下
            if attrs['sms_code'] != real_sms_code.decode():
                raise serializers.ValidationError('短信验证码错误')

        return attrs

    def create(self, validated_data):
        """重写保存方法，增加密码加密"""

        User = get_user_model()

        # 移除数据库模型类中不需要的属性
        # 删除字典数据的两种方法是
        # del 字典[key] 删除指定键值对,key不存在不会报错
        # 字典.pop(key) 删除指定键值对,key不存在会报错
        del validated_data['password2']
        del validated_data['sms_code']

        # 判断当前的用户名是不是邮箱格式
        if "@" in validated_data["username"]:
            # 用户输入的是邮箱
            validated_data["email"] = validated_data["username"]

        # user = User.objects.create(username=xxx, password=xxxx, mobile=xxxx)
        user = User.objects.create(**validated_data)

        # 将密码加密,然后保存
        user.set_password(validated_data['password'])
        user.save()

        return user
