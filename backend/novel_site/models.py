import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    '''
        自定义用户模型类
    '''
    mobile_phone = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True, unique=True)  # , unique=True
    current_ip = models.CharField(max_length=15, verbose_name='手机号', blank=True)
    # 虽然主键由setting.py中的DEFAULT_AUTO_FIELD自动生成了，但主键位数太差了，重新用uuid生成一些唯一的区别设置
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=10, verbose_name="用户身份", blank=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username