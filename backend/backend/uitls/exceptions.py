from rest_framework.views import exception_handler

from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging
# 指向的是setting.py文件中，日志配置的loggers的键
logger = logging.getLogger("django")

def custom_exception_handler(exc, context):
    pass
