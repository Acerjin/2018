# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *
class FaqCategoryAdmin(admin.ModelAdmin):
    fields = ['catname']

class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ['catname']

class ServiceCategoryAdmin(admin.ModelAdmin):
    fields = ['catname']    
    
class AboutCategoryAdmin(admin.ModelAdmin):
    fields = ['catname']   

class DownloadCategoryAdmin(admin.ModelAdmin):
    fields = ['catname']    

class AnnouncementAdmin(admin.ModelAdmin):
    fields = ['title','content','createddate']   
    
class ProductsAdmin(admin.ModelAdmin):
    fields = ['catid','product_name','product_simple_desc','product_full_desc','product_pic','product_order'] 

class NewsAdmin(admin.ModelAdmin):
    fields = ['title','content','createddate']  
class FaqAdmin(admin.ModelAdmin): 
    fields = ['catid','title','content']
admin.site.register(FaqCategory, FaqCategoryAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ServiceCategory,ServiceCategoryAdmin)
admin.site.register(AboutCategory,AboutCategoryAdmin)
admin.site.register(DownloadCategory,DownloadCategoryAdmin)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Faq,FaqAdmin)


