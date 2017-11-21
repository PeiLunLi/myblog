from django.shortcuts import render, redirect
from django.urls import reverse

from  operation.models import  EmailVerifyRecord
from users.models import UserPro


def ActiveUser(request,active_code):
    if request.method =='GET':
        print(active_code)
        # 获取激活码
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        # 筛选邮件操作的数据库表，筛选出激活码对照的数据，由于这里是filter，是个集合。
        if all_records:
            # 如果存在的话
            for records in all_records:
                email = records.email
                # 取出该实例的邮箱
                user = UserPro.objects.get(email=email)
                # 根据邮箱在用户表里面筛选处数据
                user.is_active = 1
                # 把用户状态设置称激活状态
                user.save()
                # 保存
                return redirect(reverse('users:login'))
        else:
            return redirect(reverse('users:register'))
        return redirect(reverse('users:register'))