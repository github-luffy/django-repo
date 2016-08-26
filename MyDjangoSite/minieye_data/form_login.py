# coding:utf-8

from django import forms
from MyDjangoSite.minieye_data.models import User
from django.core.exceptions import ObjectDoesNotExist
# create forms here


class UserLoginForm(forms.Form):
    username = forms.CharField(

    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    # def clean_username(self):
    #     if 'username'in self.cleaned_data:
    #         username = self.cleaned_data['username']
    #         try:
    #             User.objects.get(name=username)
    #         except ObjectDoesNotExist:
    #             raise forms.ValidationError("用户名不存在")
    #         return username


