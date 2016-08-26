# coding:utf-8
from MyDjangoSite.minieye_data.models import Car, Manager
from django.views.generic import ListView
# Create your views here.


# 使用内建视图
class CarList(ListView):
    model = Car
    template_name = 'car_list_page.html'
    context_object_name = 'car_list'

    def get_context_data(self, **kwargs):
        context = super(CarList, self).get_context_data(**kwargs)
        context['manager_list'] = Manager.objects.all()
        return context

from MyDjangoSite.minieye_data.form_register import UserInfoForm
from MyDjangoSite.minieye_data.form_login import UserLoginForm
from django.shortcuts import render_to_response, render, redirect
from django import forms
from MyDjangoSite.minieye_data.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def login(request):
    error_password = False
    error_user = False
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                User.objects.get(name=username)
            except ObjectDoesNotExist:
                error_user = True
            else:
                try:
                    User.objects.get(name=username, password=password)
                except ObjectDoesNotExist:
                    error_password = True
                else:
                    return redirect("/minieye-data/")
    else:
        form = UserLoginForm(
            # initial={'username': '请填入您的用户名',}
        )
    return render(request, "registration/login.html", locals(),)


# 使用内建注册表单
def register(request):

    def is_male_or_female(value):
        user_sex = '男'
        if value == str(1):
            user_sex = '女'
        return user_sex

    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            sex = form.cleaned_data["sex"]
            password = form.cleaned_data["password1"]
            city = form.cleaned_data["city"]
            province = form.cleaned_data["province"]
            country = form.cleaned_data["country"]
            mobile = form.cleaned_data["mobile"]
            email = form.cleaned_data["email"]
            add_user = User.objects.create(
                name=name,
                sex=is_male_or_female(sex),
                password=password,
                city=city,
                province=province,
                country=country,
                mobile=mobile,
                email=email,
            )
            add_user.save()
            return redirect("/minieye/login")
    else:
        form = UserInfoForm(

        )
    return render(request, "registration/register.html", {"form": form},)

