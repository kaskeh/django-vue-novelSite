from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="手机号码")
    avatar = models.ImageField(upload_to="avatar", blank=True, null=True, verbose_name="用户头像")
    wxchat = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name="微信号")

    class Meta:
        db_table = "nv_user"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name