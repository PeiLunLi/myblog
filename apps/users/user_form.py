from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # captcha = CaptchaField()
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空.'})
    password = forms.CharField(required=True,error_messages={'required': '密码不能为空.'})


class RegisterForm(forms.Form):

    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空.'})
    password = forms.CharField(required=True,error_messages={'required': '密码不能为空.'})
    password2 = forms.CharField(required=True, error_messages={'required': '密码不能为空.'})
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空.'})
    nick_name = forms.CharField(required=True, error_messages={'required': '昵称不能为空.'})

    def clean_password2(self):
        '''
        验证密码是否两次输入一致
        '''
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password confirm failed')
        return password2
