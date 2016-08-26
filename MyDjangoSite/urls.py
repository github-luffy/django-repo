# coding=gbk
"""MyDjangoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from MyDjangoSite.views import hello, current_datetime, hours_ahead, display_meta, unruly_passengers_csv, hello_pdf

# from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView  # Django1.10 doesn't contain list_detail
from MyDjangoSite.books.models import Publisher, Book, Author
from MyDjangoSite.minieye_data.views import CarList, register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
# # get extra context
# class PublisherDetail(DetailView):
#     model = Publisher  # queryset = Publisher.objects.all()
#     context_object_name = "publisher"
#
#     def get_context_data(self, **kwargs):
#         context = super(PublisherDetail, self).get_context_data(**kwargs)
#         context['book_list'] = Book.objects.all()
#         return context

# class PublisherBookList(ListView):
#     template_name = "books/books_by_publisher.html"
#
#     def get_queryset(self):
#         self.publisher = get_object_or_404(Publisher, name=self.args[0])
#         return Book.objects.filter(publisher=self.publisher)
#
#     def get_context_data(self, **kwargs):
#         context = super(PublisherBookList, self).get_context_data(**kwargs)
#         context['publisher'] = self.publisher
#         return context

# class BookList(ListView):
#     queryset = Book.objects.order_by("-publication_date")
#     template_name = "book_list_page.html"
#     context_object_name = "book_list"


class PublisherList(ListView):
    model = Publisher
    template_name = "publisher_list_page.html"
    context_object_name = "my_publishers"  # default name is object_list

    # get extra context   : Book and Author
    def get_context_data(self, **kwargs):
        context = super(PublisherList, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['author_list'] = Author.objects.all()
        return context

urlpatterns += [
    url(r'^publishers/$', PublisherList.as_view()),
    # url(r'^books/([\w+])/$', PublisherBookList.as_view()),
]

from django.contrib.auth.views import logout
from MyDjangoSite.minieye_data import views
# minieye_data的视图和url配置
# 使用内建的登录与退出
# /accounts/login/ 和 /accounts/logout/ 是Django提供的视图的默认URL
urlpatterns += [
    url(r'^minieye/login/$', views.login),
    url(r'^minieye/logout/$', logout),
    url(r'^minieye/register/$', views.register),
    url(r'^minieye-data/$', CarList.as_view())
]

# 测试
urlpatterns += [
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
]

from MyDjangoSite.books import views
# app:books的视图
urlpatterns += [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact-form/$', views.contact_form),
    url(r'^contact-thanks/$', views.contact_thanks)
]

# 输出非html内容
urlpatterns += [
    url(r'^passengers/$', unruly_passengers_csv),   # load csv file
    url(r'^hello-pdf/$', hello_pdf)
]
