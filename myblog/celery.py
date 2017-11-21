from __future__ import absolute_import
import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
#设置“celery”程序的默认Django设置模块
django.setup()
app = Celery('myblog')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.result_backend = 'redis://:@127.0.0.1:6379/0'