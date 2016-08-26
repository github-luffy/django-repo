# coding:utf-8


import re
from django import forms
from MyDjangoSite.minieye_data.models import User
from django.core.exceptions import ObjectDoesNotExist
# create forms here


def name_validate(name):
    name_re = re.compile(r'^[a-zA-Z]{1}([a-zA-Z0-9]|[._]){4,19}$')
    if not name_re.match(name):
        raise forms.ValidationError("只能输入5-20个以字母开头、可带数字、“_”、“.”的用户名")


def password_validate(password1):
    pass_re = re.compile(r'^(\w){8,20}$')
    if not pass_re.match(password1):
        raise forms.ValidationError("只能输入8-20个字母,数字,下划线")


def mobile_validate(mobile):
    mobile_re = re.compile(r'^(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(mobile):
        raise forms.ValidationError("手机号码格式不正确")


class UserInfoForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[name_validate, ],
    )
    user_sex_choice = (
        (0, '男'),
        (1, '女')
    )
    sex = forms.CharField(
        widget=forms.Select(choices=user_sex_choice)
    )
    password1 = forms.CharField(
        validators=[password_validate, ],
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
    )
    city = forms.CharField(
        max_length=50,
    )
    province = forms.CharField(
        max_length=50,
    )
    country = forms.CharField(
        max_length=50,
    )
    mobile = forms.CharField(
        validators=[mobile_validate, ]
    )
    email = forms.EmailField(
        required=False,
    )

    # 函数名很重要
    def clean_name(self):
        user_name = self.cleaned_data['name']
        try:
            User.objects.get(name=user_name)
        except ObjectDoesNotExist:
            return user_name
        raise forms.ValidationError("该用户名已存在")

    def clean_password2(self):
        # 确认密码是否一致
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError("密码输入不一致，请重新输入")




