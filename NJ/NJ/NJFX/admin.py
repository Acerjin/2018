# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from .models import *
# Register your models here.
class WdcpAdmin(admin.ModelAdmin): 
    list_display = ('zh','pz','mc')
    fields = ['zh','pz','mc','je','zhzb','rzzt','ztpj','zxpj','qx','syl','pzrq','dqrq','synx','lshzj','by1','sfgq']
    #def __init__(self, *args, **kwargs):
       # self.fields['zh'].queryset = Zh.objects.all()
class TzqkfxAdmin(admin.ModelAdmin):
    list_display = ( 'zhmc','rq','stzcjz', 'srhj', 'sndljlr', 'bnlr', 'ljlr', 'sndwjz', 'sndtzhdwjz', 'sqdwjz', 'dwjz', 'bqjzzjbd', 'bnsyl', 'jz', 'ljpm', 'bnpm')
    fields= [ 'rq','zhmc','stzcjz', 'srhj', 'sndljlr', 'bnlr', 'ljlr', 'sndwjz', 'sndtzhdwjz', 'sqdwjz', 'dwjz', 'bqjzzjbd', 'bnsyl', 'jz', 'ljpm', 'bnpm']
class NjzhAdmin(admin.ModelAdmin): 
    fields = ['zhmc','zhje','zhsj','zhll']
class PzAdmin(admin.ModelAdmin): 
    fields = ['pz']
class CtglAdmin(admin.ModelAdmin):
    list_display = ('cpmc','lb','zhmc')
    fields = ['lb','rq', 'zhmc', 'cpmc', 'gm', 'zb', 'zcfb', 'xyfb1', 'xyfb2', 'xyfb3', 'xyfb4', 'qyzb', 'ggb', 'dwjz', 'synx', 'fxzkpg', 'fkcs', 'bz']
admin.site.register(Wdcp,WdcpAdmin)
admin.site.register(Njzh,NjzhAdmin)
admin.site.register(Pz,PzAdmin)
admin.site.register(Tzqkfx,TzqkfxAdmin)
admin.site.register(Ctgl,CtglAdmin)
