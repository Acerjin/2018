"""pro9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#coding:utf-8
from django.conf.urls import  include, url
from django.contrib import admin
from app1 import views
admin.autodiscover()

urlpatterns = [  
    url(r'^$',views.index),
    url(r'^faq$', views.faq),
    url(r'^faq/(?P<catid>\d{1,15})$', views.faq_cat_detail),
    url(r'^about$', views.about),
    url(r'^about/(?P<catid>\d{1,15})$', views.about_cat_detail),
    url(r'^service$', views.service),
    url(r'^service/(?P<catid>\d{1,15})$', views.service_cat_detail),
    url(r'^product$', views.products),
    url(r'^product/(?P<catid>\d{1,15})$', views.product_cat_detail),
    url(r'^download$', views.download),
    url(r'^download/(?P<catid>\d{1,15})$', views.download_cat_detail),
    url(r'^news/$', views.news),
    url(r'^news/(?P<newsid>\d{1,15})$', views.news_detail),
    url(r'^admin/', include(admin.site.urls)),
 
#     url(r'^savecomment', 'addcomment'),
#     url(r'^tags/(?P<category>.+)/(?P<mytag>.+)$', 'tags'),
#     url(r'^search/$', 'search'),
#     url(r'^message/$', 'me'),
    ]
