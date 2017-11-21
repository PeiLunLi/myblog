__author__ = 'Luo'

from operation.models import EmailVerifyRecord
from uuid import uuid4
from myblog.settings import EMAIL_FROM
from myblog.celery import app


@app.task
def send_email_tools(email, send_type=0):
    print('发送')
    # TODO 记得将发送的激活链接修改成访问的服务器的 IP 或者域名
    email_record = EmailVerifyRecord()
    code = random_str()
    # 用户注册邮件中的信息，赋值到 model 实例中
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 发送的邮件内容逻辑
    email_title = ""
    email_body = ""

    # 注册类邮件内容
    if send_type == "register":
        email_title = "用户注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/operation/active/{0}".format(code)
    elif send_type == "forget":
        email_title = "忘记密码链接"
        email_body = "请点击下面的链接修改密码：http://127.0.0.1:8000/users/forget/{0}".format(code)
    from django.core.mail import send_mail

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        # TODO 记得修改
        print("邮件发送成功")

def random_str():
    # 用 uuid.uuid4() 生成 36 位的随机uuid，再用 str() 转化成字符串
    return str(uuid4())
