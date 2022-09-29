from django.db import models

class BaseModel(object):
    """基础模型，将部分重复的字段通过继承的方式添加"""
    CREATED_BY = models.CharField(max_length=20,
                                  null=False,
                                  verbose_name="创建人")
    # auto_now_add=True，设置只记录第一次创建的时间，后续不会进行时间上的变更
    CREATED_TIME = models.DateTimeField(auto_now_add=True)
    UPDATED_BY = models.CharField(max_length=20,
                                  null=False,
                                  verbose_name="更新人")
    # auto_now=True，设置当每次更新时，都以当前时间记录
    UPDATED_TIME = models.DateTimeField(auto_now=True)