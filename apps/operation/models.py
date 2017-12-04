from datetime import datetime

from django.db import models

# Create your models here.


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="邮箱验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="注册类型", choices=(('register', '注册'), ('forget', '忘记密码')), max_length=20)
    send_time = models.DateTimeField(verbose_name="注册时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
