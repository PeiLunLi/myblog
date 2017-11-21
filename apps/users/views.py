import os

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout

import md5utils
from myblog import settings
from users.models import UserPro
from .user_form import LoginForm,RegisterForm
from email_send import send_email_tools
#自定义验证
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户在 model 中是否存在，用 get 可以确保只有一个该用户
            user = UserPro.objects.get(Q(username=username)|Q(email=username))
            # 传入的密码，与 model 中的对比，只能使用 check_password 方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# Create your views here.
def logoff(request):
    if request.user.is_authenticated():
        print('退出了')
        logout(request)
        return redirect(reverse('home'))

def User_login(request):

    if request.method =='POST':
        objPost = LoginForm(request.POST)
        if objPost.is_valid():
            username =request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=username, password=password)
            # 判断是否成功匹配上
            if user is not None:
                if user.is_active == 0:
                    return render(request, 'users/login.html', {'msg': '用户未激活！'})
                login(request,user)
                return redirect(reverse('home'))
            else:
                return render(request,'users/login.html',{'msg':'用户名或密码错误'})
        else:
            return render(request, 'users/login.html', {'form':objPost})

    else:

        return render(request, 'users/login.html')
def register(request):
    if request.method =="GET":
        return render(request,'users/register.html')
    elif request.method =='POST':
        objPost = RegisterForm(request.POST)
        if objPost.is_valid():
            username = request.POST.get('username', '')
            #用户名不允许重复
            password = request.POST.get('password', '')
            email =request.POST.get('email','')
            #邮箱不允许重复
            nick_name =request.POST.get('nick_name','')
            image = request.FILES.get("image")

            # file_name = image.name  # 文件名
            file_content = image.read()  # 读取上传文件所有内容
            path = os.path.join("image/" + md5utils.getMD5(file_content))
            filePath = os.path.join(settings.MEDIA_ROOT, path)
            if image.multiple_chunks():  # 判断文件是否过大 2.5M为标准
                with open(filePath, 'wb') as f:
                    for chunk in image.chunks():  # 大文件分块写入文件
                        f.write(chunk)
            else:
                with open(filePath, 'wb') as f:
                    f.write(file_content)
            try:
                user = UserPro()
                user.username = username
                user.password = make_password(password)
                user.email = email
                user.nick_name = nick_name
                user.image = path
                user.is_active =0
                user.save()
                send_email_tools.delay(email, "register")
                return render(request,'operation/send_email_ok.html',{'email':email})
            except Exception as e:
                print(str(e))
                return render(request, 'users/register.html', {'msg': '未知错误'})
        return render(request, 'users/register.html', {'form': objPost})


