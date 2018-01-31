#coding:utf-8
'''
Created on 2013-11-11
@author: Administrator
'''
from django.conf import settings


#from django.core.context_processors import csrf


from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import *


def index(request):
    context={}
    #context.update(csrf(request))
    webname =settings.WEB_NAME
    return render_to_response('index.html',{'webname':webname})    


def faq(request): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cats = FaqCategory.objects.order_by('id')[0:1]
    
    if cats:
        catname = cats[0].catname
        print catname
        faqs = Faq.objects.filter(catid=cats[0].id).order_by("id")
        #context['faqs'] = faqs
        print faqs
    
    return render_to_response('faq.html',{'catname':catname,'faqs':faqs})

def faq_cat_detail(request,catid):
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cat =FaqCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    faqs =Faq.objects.filter(catid=catid).order_by("id")
    context['faqs'] = faqs
    return render_to_response('faq.html',context,RequestContext(request))

def about(request): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cats = AboutCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        abouts = About.objects.filter(catid=cats[0].id).order_by("id")
        context['abouts'] = abouts
    return render_to_response('about.html',context,RequestContext(request))

def about_cat_detail(request,catid): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cat =AboutCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    abouts =About.objects.filter(catid=catid).order_by("id")
    context['abouts'] = abouts
    return render_to_response('about.html',context,RequestContext(request))

def service(request): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cats =ServiceCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        services =Service.objects.filter(catid=cats[0].id).order_by("id")
        context['services'] = services
    return render_to_response('service.html',context,RequestContext(request))

def service_cat_detail(request,catid): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cat =ServiceCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    services =Service.objects.filter(catid=catid).order_by("id")
    context['services'] = services 
    return render_to_response('service.html',context,RequestContext(request))

def products(request): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cats =ProductCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        products =Products.objects.filter(catid=cats[0].id).order_by("id")
        context['products'] = products
    return render_to_response('products.html',context,RequestContext(request))

def product_cat_detail(request,catid): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cat =ProductCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    products =Products.objects.filter(catid=catid).order_by("id")
    context['products'] = products
    return render_to_response('products.html',context,RequestContext(request))

def download(request): 
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cats =DownloadCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        downloads =Download.objects.filter(catid=cats[0].id).order_by("id")
        context['downloads'] = downloads
    return render_to_response('download.html',context,RequestContext(request))

def download_cat_detail(request,catid):
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME
    cat =DownloadCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    downloads =Download.objects.filter(catid=catid).order_by("id")
    context['downloads'] = downloads
    return render_to_response('download.html',context,RequestContext(request))

def news(request):
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME  
    news = News.objects.all()
    context['items'] = news 
    return render_to_response('news.html',context,RequestContext(request))

def news_detail(request,newsid):
    context={}
    #context.update(csrf(request))
    webname=settings.WEB_NAME  
    news =News.objects.get(id = newsid) 
    context['news'] = news
    return render_to_response('news_detail.html',context,RequestContext(request))
    
    
