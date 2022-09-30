from celery import Celery

# 创建celery 主程序对象
app = Celery("novelSite")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
import django
django.setup()

# 加载配置，通过app对象加载配置
app.config_from_object("myCelery.config")

# 注册任务
# 自动搜索并加载任务
# 参数必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["mycelery.email", "mycelery.cache"])
app.autodiscover_tasks(["myCelery.mail"])

# 通过终端来启动celery
# 强烈建议切换目录到项目的根目录下启动celery
# celery -A mycelery.main worker --loglevel=info
