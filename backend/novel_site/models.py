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


# 作者表
class authors(models.Model):
    author_id = models.CharField(max_length=20,
                                 null=False,
                                 verbose_name='作者编号',
                                 unique=True
                                 )
    author_name = models.CharField(max_length=20,
                                   null=False,
                                   verbose_name="作者名称")

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

    def __str__(self):
        return self.author_name

    class Meta:
        # 设置表名
        db_table = "authors"

# 小说表
class novel(models.Model):
    novel_number = models.CharField(max_length=20,
                                    verbose_name="小说编号",
                                    null=False,
                                    unique=True)
    novel_name = models.CharField(max_length=20,
                                    verbose_name="小说名称",
                                    null=False)
    novel_page_count = models.IntegerField(default=0,
                                  verbose_name="小说当前章节数",
                                  null=False)
    # 0：完结，1：连载中，2：断更
    novel_status = models.CharField(max_length=1,
                                  verbose_name="小说当前状态",
                                  null=False)
    novel_cate = models.CharField(max_length=1,
                                    verbose_name="小说分类",
                                    null=False)
    novel_surface_img = models.CharField(max_length=255,
                                  verbose_name="小说封面保存地址",
                                  null=False)
    novel_author = models.CharField(max_length=20,
                                         verbose_name="小说作者",
                                         null=False)
    novel_description = models.CharField(max_length=255,
                                    verbose_name="小说描述",
                                    null=False)

    # 外键
    author_fk = models.ForeignKey("authors", on_delete=models.CASCADE)


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

    def __str__(self):
        return self.novel_name

    class Meta:
        # 设置表名
        db_table = "novel"

# 小说章节表
class novels(models.Model):
    novel_number = models.CharField(max_length=20,
                                  verbose_name="小说编号",
                                  null=False)
    novel_page_name = models.CharField(max_length=50,
                                  verbose_name="章节名称",
                                  null=False)
    novel_page_num = models.CharField(max_length=20,
                                       verbose_name="章节编号",
                                       null=False)
    novel_content = models.TextField(verbose_name="小说内容",
                                      null=False)

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

    # 外键
    novel_fk = models.ForeignKey("novel", on_delete=models.CASCADE)

    def __str__(self):
        return self.novel_page_name

    class Meta:
        # 设置表名
        db_table = "novels"