#coding:utf-8
'''
Created on 2013-11-11
@author: Administrator
'''
from __future__ import unicode_literals


from django.db import models
import time

class FaqCategory(models.Model):
    #id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 't_faq_category'
        verbose_name = u'faq_category'
        verbose_name_plural = u'faq_category'
        app_label = u'My_Category'
    def __unicode__(self):
        return self.catname
        
class ProductCategory(models.Model):
    #id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 't_product_category'
        verbose_name = u'product_category'
        verbose_name_plural = u'product_category'
        app_label = u'My_Category'
    def __unicode__(self):
        return self.catname

class ServiceCategory(models.Model):
   # id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 't_service_category'
        verbose_name = u'service_category'
        verbose_name_plural = u'service_category'
        app_label = u'My_Category'
    def __unicode__(self):
        return self.catname
        
class AboutCategory(models.Model):
    #id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 't_about_category'
        verbose_name = u'about_category'
        verbose_name_plural = u'about_category'
        app_label = u'My_Category'
    def __unicode__(self):
        return self.catname
        
class DownloadCategory(models.Model):
   # id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=150L, blank=True)
    class Meta:
        db_table = 't_download_category'
        verbose_name = u'download_category'
        verbose_name_plural = u'download_category'
        app_label = u'My_Category'
    def __unicode__(self):
        return self.catname

class Announcement(models.Model):
   # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100L , blank = False , verbose_name = "Title")
    content = models.TextField( blank = False , verbose_name = "Content")
    createddate = models.DateField(null=True, db_column='createdDate', blank=True , default=time.strftime('%Y-%m-%d'),verbose_name='Date')
    class Meta:
        db_table = u't_announcement'
        verbose_name = u'announcement'
        verbose_name_plural = u'announcement'
        app_label = u'My_Company'
        
class Products(models.Model):
    #id = models.IntegerField(primary_key=True)
    catid = models.ForeignKey(ProductCategory,db_column= 'catid',to_field='id',blank=False,verbose_name = 'catid') 
    product_name = models.CharField(max_length=200L , verbose_name = "Name")
    product_simple_desc = models.TextField(blank=True , verbose_name = "Simple Desc")
    product_full_desc = models.TextField(blank=True , verbose_name = "Full Desc")
    product_pic = models.CharField(max_length=200L, blank=True , verbose_name = "Picture Path")
    product_order = models.IntegerField(verbose_name = "Order")
    createddate = models.DateField(db_column='createdDate', blank=True , default=time.strftime('%Y-%m-%d') , verbose_name = "Created Date") # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 't_products'
        verbose_name = u'products'
        verbose_name_plural = u'products'
        app_label = u'My_Company'

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255L, blank=True ,verbose_name = "Title")
    content = models.TextField(blank=True , verbose_name = "Content")
    createddate = models.DateField(null=True, db_column='createdDate', blank=True , default=time.strftime('%Y-%m-%d') , verbose_name = "Created Date") # Field name made lowercase.
    class Meta:
        db_table = 't_news'
        verbose_name = u'news'
        verbose_name_plural = u'news'
        app_label = u'My_Company'
        
class Download(models.Model):
   #id = models.AutoField(primary_key=True)
    catid = models.ForeignKey(DownloadCategory,db_column= 'catid',to_field='id',blank=False,verbose_name = 'catid') 
    title = models.CharField(max_length=150L, blank=True)
    content = models.TextField(blank=True)
    downloadurl = models.CharField(max_length=200L, blank=True)
    createddate = models.DateField(null=True, db_column='createdDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 't_download'
        verbose_name = u'download'
        verbose_name_plural = u'download'
        app_label=u"My_Company"
        
class Faq(models.Model):
   # id = models.AutoField(primary_key=True)
    catid = models.ForeignKey(FaqCategory,db_column= 'catid',to_field='id',blank=False,verbose_name = 'catid')    
    title = models.CharField(max_length=150L, blank=True ,verbose_name = 'title')
    content = models.TextField(blank=True,verbose_name = 'content')
    class Meta:
        db_table = 't_faq'
        verbose_name = u'faq'
        verbose_name_plural = u'faq'
        app_label=u"My_Company"
        
class Service(models.Model):
   # id = models.AutoField(primary_key=True)
    catid = models.ForeignKey(ServiceCategory,db_column= 'catid',to_field='id',blank=False,verbose_name = 'catid') 
    title = models.CharField(max_length=150L, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = 't_service'
        verbose_name = u'service'
        verbose_name_plural = u'service'
        app_label=u"My_Company"
        
class About(models.Model):
   # id = models.AutoField(primary_key=True)
    catid = models.ForeignKey(AboutCategory,db_column= 'catid',to_field='id',blank=False,verbose_name = 'catid') 
    title = models.CharField(max_length=150L, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = 't_about' 
        verbose_name = u'about'
        verbose_name_plural = u'about'
        app_label=u"My_Company"