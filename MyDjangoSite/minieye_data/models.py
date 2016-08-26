# coding=gbk
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    password = models.CharField(max_length=50, )
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.FloatField()

    def __unicode__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50)
    work_city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.email)

    class Meta:
        ordering = ['name']     # 按姓名排序


class Car(models.Model):
    cid = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    card_number = models.IntegerField()
    total_capacity = models.FloatField()
    manager = models.ForeignKey(Manager)
    data_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u"%d %s%s" % (self.cid, self.city, self.category)

    class Meta:
        ordering = ['cid']   # 按编号排序
