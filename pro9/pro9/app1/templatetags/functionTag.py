#coding:utf-8
'''
Created on 2013-11-5
@author: lzs
Powered for yihaomen.com
注意: 这些TAG 中如果有分类 的，都写在 kwargs中。由前端模板传入分数筛选.
'''



from django.conf import settings
from django import template
from app1 import models
register = template.Library()

""" 系统首页，在slide 图片 """
@register.inclusion_tag('widget/announce_widget.html',name='display_index_announce_widget')
def index_announce(**kwargs):
    try:
        rows = models.Announcement.objects.order_by("-id")[0:2].values('id','title','content','createddate')
    except ValueError:
        rows = None
    return {'announces' : rows}

@register.inclusion_tag('widget/products_widget.html',name='display_products_widget')
def show_products(**kwargs):
    try:
        rows = models.Products.objects.order_by("product_order").values('id','product_name','product_simple_desc','createddate')
    except ValueError:
        rows = None
    return {'products' : rows}

@register.inclusion_tag('widget/news_widget.html',name='display_index_news_widget')
def index_news(**kwargs):
    try:
        rows = models.News.objects.order_by("-id").values('id','title','content','createddate')
        cats = models.AboutCategory.objects.order_by('id')[0:1]
        about = None
        if cats:            
            abouts = models.About.objects.filter(catid=cats[0].id).order_by("id")[0:1].values('id','catid','content')
            if abouts:
                about = abouts[0]            
    except ValueError:
        rows = None
    return {'news' : rows,'about':about}

@register.inclusion_tag('widget/category_widget.html',name='display_faq_category_widget')
def show_faq_category(**kwargs):
    try:
        rows = models.FaqCategory.objects.order_by("id").values('id','catname')
    except ValueError:
        rows = None
    return {'cats' : rows,'pic':'faq'}

@register.inclusion_tag('widget/category_widget.html',name='display_product_category_widget')
def show_products_category(**kwargs):
    try:
        rows = models.ProductCategory.objects.order_by("id").values('id','catname')
    except ValueError:
        rows = None
    return {'cats' : rows,'pic':'product'}

@register.inclusion_tag('widget/category_widget.html',name='display_service_category_widget')
def show_service_category(**kwargs):
    try:
        rows = models.ServiceCategory.objects.order_by("id").values('id','catname')
    except ValueError:
        rows = None
    return {'cats' : rows,'pic':'service'}

@register.inclusion_tag('widget/category_widget.html',name='display_about_category_widget')
def show_about_category(**kwargs):
    try:
        rows = models.AboutCategory.objects.order_by("id").values('id','catname')
    except ValueError:
        rows = None
    return {'cats' : rows,'pic':'about'}

@register.inclusion_tag('widget/category_widget.html',name='display_download_category_widget')
def show_download_category(**kwargs):
    try:
        rows = models.DownloadCategory.objects.order_by("id").values('id','catname')
    except ValueError:
        rows = None
    return {'cats' : rows,'pic':'download'}

@register.inclusion_tag('widget/index_faqs_widget.html',name='display_index_recent_faqs')
def index_recent_faqs(**kwargs):
    try:
        rows = models.Faq.objects.order_by("-id").values('id','catid','title')[0:5]
    except ValueError:
        rows = None
    return {'recentFaqs' : rows}
