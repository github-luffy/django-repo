# coding=gbk
from django.contrib import admin
from MyDjangoSite.minieye_data.models import User, Card, Manager, Car
# Register your models here.


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_city', 'address', 'email')
    fields = ('name', 'address', 'work_city', 'province', 'country', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'work_city', 'address', 'email')


class CarAdmin(admin.ModelAdmin):
    list_display = ('cid', 'city', 'category', 'usage', 'card_number', 'total_capacity', 'manager', 'data_date')
    fields = ('cid', 'city', 'category', 'usage', 'card_number', 'total_capacity', 'manager', 'data_date')  # 可以防止信息被修改
    list_filter = ('cid', 'manager')
    date_hierarchy = 'data_date'
    search_fields = ('cid', 'city')
    ordering = ('data_date',)    # 按日期排序
    raw_id_fields = ('manager',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'password', 'city', 'province', 'country', 'mobile', 'email')
    ordering = ('name',)

admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Car, CarAdmin)
