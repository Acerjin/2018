# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os 
from _ast import Pass
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NJ.settings") 
import django

if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


import xlrd
import re
import cx_Oracle

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import connection,transaction
from django.conf import settings


# Create your views here.
def index(request,):
    #timenow =  timezone.now()
    now = datetime.datetime.now()
    newnow = now.strftime("%Y-%m-%d")
    addday = timedelta(days=30)
    newrq = (now+addday).strftime("%Y-%m-%d")
    cursor1 = connection.cursor()
    #cursor.execute("select a.id,b.zh,c.pz pz,mc,je,round(a.je*100/b.zhje,2) zhzb,ifnull(rzzt,''),ifnull(ztpj,''),ifnull(zxpj,''),ifnull(qx,''),ifnull(syl,''),pzrq,dqrq,ifnull(synx,''),ifnull(lshzj,''),(case when a.dqrq <%s  then '1' else  '0' end ) ifgq,by1 from njfx_wdcp a,njfx_zh b,njfx_pz c where a.zh_id=b.id and a.pz_id=c.id and a.dqrq >%s",[newrq,newnow])
    cursor1.execute("select a.id,b.zhmc,c.pz pz,mc,je,round(a.je*100/b.zhje,2) zhzb,rzzt,ztpj,zxpj,qx,syl,pzrq,dqrq,synx,lshzj,(case when a.dqrq <%s  then '1' else  '0' end ) ifgq,by1,case  when sfgq='1' then '提前到期' else  '' end as sfgq from njfx_wdcp a,njfx_njzh b,njfx_pz c where a.zh_id=b.id and a.pz_id=c.id and a.dqrq >%s",[newrq,newnow])

    #col_names = [desc[0] for desc in cursor.description]
    #print col_names
    wdcp = cursor1.fetchall()
    cursor1.close()
    
    #wdcp = dict(zip(col_names, wdcp))
    #wdcp = Wdcp.objects.raw("select a.id,zh,c.pz pz,mc,je,round(a.je*100/b.zhje,2) zhzb,rzzt,ztpj,zxpj,qx, syl,dqrq,synx,by1,lshzj,pzrq,(case when a.dqrq <%s  then '1' else  '0' end ) ifgq from njfx_wdcp a,njfx_zh b,njfx_pz c where a.zh_id=b.id and a.pz_id=c.id and a.dqrq >%s",[newrq,newnow])
    #wdcp = Wdcp.objects.raw('select id,zh,pz,mc,je,zhzb,rzzt,ztpj,zxpj,qx,syl,dqrq,synx,by1,lshzj,pzrq from njfx_wdcp where dqrq > %s',[newrq]) 
    cursor2 = connection.cursor()
    cursor2.execute("select count(id) gqcount from njfx_wdcp where dqrq < %s and dqrq > %s",[newrq,newnow])
    gqcount = cursor2.fetchall()
    gc = gqcount[0][0]
    print gc
    request.session['gc']= gc
    cursor2.close()

    #print gqcount
    
    return render_to_response('index.html', {'wdcp':wdcp,'gqcount':gc})
def hz(request):
    now = datetime.datetime.now()
    newnow = now.strftime("%Y-%m-%d")
    #各有效组合的总金额
    cursor1 = connection.cursor()
    cursor1.execute('select round(sum(b.zhje),2) zh from njfx_njzh b where b.id in (select zh_id from njfx_wdcp a where a.dqrq>%s )',[newnow])
    zh_temp = cursor1.fetchone()
    cursor1.close()
    
    
    #zh = Wdcp.objects.raw('select b.zh, round(sum(b.zhje),2) zh1 from njfx_zh b where b.zh in (select zh_id from njfx_wdcp a where a.dqrq> %s )',[newnow])
    #test1 = zh[0].zh    
    zh = zh_temp[0]
    print zh,newnow
    # 各组合所占比例
    cursor2 = connection.cursor()
    cursor2.execute('select b.zhmc,sum(a.je) hzje, round(sum(a.je)*100/%s,2) zhzb,sum(a.lshzj) hzlshzj from  njfx_wdcp a,njfx_njzh b where  a.dqrq>%s and b.id=a.zh_id group by b.zhmc',[zh,newnow])
    zhhz = cursor2.fetchall()
    cursor2.close()
    #各品种所占比例
    cursor3  = connection.cursor()
    cursor3.execute('select b.pz,sum(a.je) hzje,round(sum(a.je)*100/%s,2) zhzb,sum(lshzj) hzlshzj from njfx_wdcp a,njfx_pz b where a.pz_id=b.id and  dqrq > %s group by b.pz ',[zh,newnow])
    pzhz =  cursor3.fetchall()
    cursor3.close()
    return render_to_response('hz.html',{'zhhz':zhhz,'pzhz':pzhz})
def excel(request):
     #excel读工具
    
    data= xlrd.open_workbook('media/1.xls') #打开文件
    table = data.sheet_by_index(0) #获取工作表
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(2)
    sheetdata =[]
    #print nrows,ncols,colnames
    for r in xrange(0,nrows):
        sheetdata.append(table.row_values(r))
    print r,'====',sheetdata
    return render_to_response('njtzfx.html',{'colnames':sheetdata})
def data_import(request):
    if request.method == 'POST':  
        file_obj = request.FILES.getlist('upfile', None)        
        if file_obj == None:
            return HttpResponse('xxx')
        else:   
            #fname= file_obj.name
            cursor1 = connection.cursor() 
            b1= '归因分析表'
            b2= '资产分布表'
            b3='资产情况表'
            b4='日均持仓'
            b5='TA'
            b6='两费'
            b7='净值'
            errortab=[]
            errorrow=[]
            for f in file_obj:
                fname = f.name
                blx1 = re.findall(b1, fname) # 表类型判断
                blx2 = re.findall(b2, fname)
                blx3 = re.findall(b3, fname)
                blx4 = re.findall(b4, fname)
                blx5 = re.findall(b5, fname)
                blx6 = re.findall(b6, fname)
                blx7 = re.findall(b7, fname)
                if blx1:   # 归因分析表
                    strsql = 'insert into NJFX_GYFX(ksrq,jsrq,tgh,zh,zclb,zcmc,sye1_bqlj,sye1_bqsyzb,sye1_bnlj,sye1_bnsyzb,sye2_bqlj,sye2_bnlj,tzsyl_bqlj,tzsyl_bnlj,drrq) values('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    tgh = table.cell(1,5).value
                    zh = table.cell(1,6).value
                    rq = table.cell(1,3).value
                    ksrq = rq[0:11]
                    jsrq = rq[-11:]
                    data = ''
                    sql1 = ''
                    nrownonullnum = 0
                    for n in range(4,nrows): #从第五行开始读
                        if table.cell(n,0).value != '': #处理合并单元格问题
                            nrownonullnum =n
                        for c in range(0,10):  
                            if  n > 4 and c== 0 and table.cell(n,c).value == '':
                                celldata = table.cell(nrownonullnum,0).value 
                                #print 'null',n,k,c,nrownonullnum,celldata                               
                            else:                                
                                celldata = table.cell(n,c).value
                                #print n,k,c,nrownonullnum,celldata 
                                #print n,k,c,celldata                
                            data += '\'%s\',' %(celldata) 
                            now = datetime.datetime.now()
                            now = str(now)[:-7]
                            import_time = '\'%s\'' %(now) 
                            print import_time
                        sql1 = strsql+'\''+ksrq+'\','+'\''+jsrq+'\','+'\''+tgh+'\','+'\''+zh+'\','+data +import_time+')' 
                        data = '' 
                        try:
                            cursor1.execute(sql1)
                        except Exception:
                            pass
                        finally:
                            sql1 =''
                elif blx2:  #资产分布表
                    strsql = 'insert into NJFX_zcfbb(rq, zh, zclb, zcmc, sz, zjzcbl,drrq) values('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    #tgh = table.cell(1,5).value
                    zh = table.cell(1,1).value
                    rq = table.cell(1,0).value
                    #ksrq = rq[0:11]
                    #jsrq = rq[-11:]
                    
                    #print rq,'|||||',zh
                    data = ''
                    sql1 = ''
                    nrownonullnum = 0
                    
                    
                    for n in range(3,nrows-1): #从第四行开始读
                        if table.cell(n,0).value != '': #处理合并单元格问题
                            nrownonullnum =n
                        if table.cell(n,4).value != '': #处理合并单元格问题
                            nrownonullnum1 =n
                        for c in range(0,4):  
                            if  n > 3 and c== 0 and table.cell(n,c).value == '':
                                celldata = table.cell(nrownonullnum,0).value 
                                #print 'null',n,k,c,nrownonullnum,celldata 
                            #elif n > 3 and c== 4 and table.cell(n,c).value == '':
                            #    celldata = table.cell(nrownonullnum1,4).value 
                                            
                            else:                                
                                celldata = table.cell(n,c).value
                                #print n,k,c,nrownonullnum,celldata 
                                #print n,k,c,celldata                
                            data += '\'%s\',' %(celldata)        
                        now = datetime.datetime.now()
                        now = str(now)[:-7]
                        import_time = '\'%s\'' %(now) 
                        #print import_time
                        
                        sql1 = strsql+'\''+rq+'\','+'\''+zh+'\','+data +import_time+')' 
                        data = '' 
                        try:
                            cursor1.execute(sql1)
                        except Exception:
                            pass
                        finally:
                            sql1 =''                                                   
                    #print sql2
                elif blx3:  #处理资产情况表
                    strsql = 'insert into NJFX_zcqkb(rq, tzzhdm, zhmc, dwjz, stzcjz, zcfe, wtje, jsy,drrq) values('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    data = ''
                    sql1 = ''
                    rq = table.cell(2, 0).value
                    print rq
                    for n in range(4,nrows): #从第四行开始读
                        if table.cell(n, 0).ctype == 3: # 3 means 'xldate' , 1 means 'text'
                            # Correct option 1
                            ms_date_number = table.cell(n,0).value # Correct option 2                        
                            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,wb.datemode)
                            py_date = datetime.datetime(year, month, day)
                            rq = str(py_date)[0:10]
                            print rq,py_date
                        for c in range(1,ncols):  
                            celldata = table.cell(n,c).value
                            #print celldata
                                #print n,k,c,nrownonullnum,celldata 
                                #print n,k,c,celldata                
                            data += '\'%s\',' %(celldata)        
                        now = datetime.datetime.now()
                        now = str(now)[:-7]
                        import_time = '\'%s\'' %(now) 
                        #print import_time
                        #print data
                        sql1 = strsql+'\''+rq+'\','+data +import_time+')' 
                        data = ''         
                        try:
                            cursor1.execute(sql1)
                        except Exception:
                            pass
                        finally:
                            sql1 ='' 
                elif blx4: #日均持仓表
                    strsql = 'insert into NJFX_ZCFBBrjcc(ksrq, jsrq, zh, zclb, zcmc, rjcccb, rjccye, drrq) values('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    data = ''
                    sql1 = ''
                    rq_temp = table.cell(2, 0).value
                    rq = rq_temp[0:23]
                    zh_temp = rq_temp.split('-')[2].split('__')
                    ksrq = rq[0:11]
                    jsrq = rq[-11:]
                    zh = zh_temp[0:1][0]
                    print rq,ksrq,jsrq,zh_temp,zh
                    tabh1 = table.cell(4, 1).value.find('日均持仓')
                    nrownonullnum = 0
                    if tabh1:
                        for n in range(5,nrows): #从第四行开始读
                            if table.cell(n,0).value != '': #处理合并单元格问题
                                nrownonullnum =n
                            for c in range(0,4):  
                                if  n > 5 and c== 0 and table.cell(n,c).value == '':
                                    celldata = table.cell(nrownonullnum,0).value 
                                    #print 'null',n,k,c,nrownonullnum,celldata 
                                #elif n > 3 and c== 4 and table.cell(n,c).value == '':
                                #    celldata = table.cell(nrownonullnum1,4).value 
                
                                else:                                
                                    celldata = table.cell(n,c).value
                                    #print n,k,c,nrownonullnum,celldata 
                                    #print n,k,c,celldata                
                                data += '\'%s\',' %(celldata)        
                            now = datetime.datetime.now()
                            now = str(now)[:-7]
                            import_time = '\'%s\'' %(now) 
                            #print import_time
                
                            sql1 = strsql+'\''+ksrq+'\','+'\''+jsrq+'\','+'\''+zh+'\','+data +import_time+')' 
                            data = ''          
                            try:
                                cursor1.execute(sql1)
                            except Exception:
                                pass
                            finally:
                                sql1 =''
                    else:
                        errmsg = '表头不符合' 
                        print errmsg 
                elif blx5: #TA数据表
                    strsql = 'insert into njfx_ta  (zh,rq, bz, slje,jzrq, xspzrq, drrq) values('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    data = ''
                    sql1 = ''
                    #print table.cell(0, 3).value
                    tabh1 = table.cell(0, 3).value.find('业务')
                    print 'ddd',tabh1
                    if tabh1:
                        for n in range(1,nrows):
                            for c in range(1,7):
                                data +='\'%s\',' %(table.cell(n,c).value)
                                now = datetime.datetime.now()
                                now = str(now)[:-7]
                                import_time = '\'%s\'' %(now)   
                            print data
                            sql1 = strsql+data+import_time+')' 
                            print sql1
                            data=''
                            try:
                                cursor1.execute(sql1)
                            except Exception as error:
                                print error
                            finally:
                                sql1 =''
                    else:
                        print "表头不对"
                    
                elif blx6: #资产净值及收益率表
                    strsql = 'insert into njfx_syl  (rq, zhmc, zh1zc, zh2zc, zh3zc, zh4zc, zhhj, tabd, tabdje, bdhzhhj, syl, drrq) values  ('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    data = ''
                    sql1 = '' 
                    for n in range(1,nrows):
                        if table.cell(n, 0).ctype == 3: # 3 means 'xldate' , 1 means 'text'
                            # Correct option 1
                            ms_date_number = table.cell(n,0).value # Correct option 2                        
                            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,wb.datemode)
                            py_date = datetime.datetime(year, month, day)
                            data = str(py_date)[0:10]
                            data = '\'%s\',' %(data) 
                        else:
                            data=table.cell(n,0).value
                            data = '\'%s\',' %(data)
                        for c in range(1,11):
                            data +='\'%s\',' %(table.cell(n,c).value)
                            now = datetime.datetime.now()
                            now = str(now)[:-7]
                            import_time = '\'%s\'' %(now)   
                        #print data
                        sql1 = strsql+data+import_time+')' 
                        data=''
                        try:
                            cursor1.execute(sql1)
                        except Exception:
                            pass
                        finally:
                            sql1 ='' 
                elif blx7: #当期资产净值浏览表
                    strsql = 'insert into njfx_zcjz  (rq, zh, slje, drrq) values ('
                    wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                    table = wb.sheet_by_index(0) #获取工作表
                    nrows = table.nrows #行数
                    ncols = table.ncols #列数
                    data = ''
                    sql1 = ''                        
                    tabname= table.cell(0,0).value
                    tabnamecheck = re.findall('资产净值',tabname)
                    if tabnamecheck:
                        for n in range(3,nrows):
                            if table.cell(n, 0).ctype == 3: # 3 means 'xldate' , 1 means 'text'
                                # Correct option 1
                                ms_date_number = table.cell(n,0).value # Correct option 2                        
                                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,wb.datemode)
                                py_date = datetime.datetime(year, month, day)
                                rq = str(py_date)[0:10]
                            else:
                                rq = table.cell(n,0).value
                            for c in range(1,3):
                                data +='\'%s\',' %(table.cell(n,c).value)
                                now = datetime.datetime.now()
                                now = str(now)[:-7]
                                import_time = '\'%s\'' %(now) 
                            sql1 = strsql+'\''+rq+'\','+data+import_time+')' 
                            data=''
                            try:
                                cursor1.execute(sql1) 
                            except  Exception as error:
                                print error
                                sql1 =''                         
                        
                else:   
                    print "表名不对"                       
        cursor1.close() 
        sql1 = '' 
        return render_to_response('sjdr.html', {'errorrow':errorrow,'errortab':errortab})         
            #return HttpResponseRedirect('/tghsj/zcqkb/?rq='+rq)
    else:
        return render_to_response('sjdr.html', {})

def tghsj(request):
    rq = request.GET.get('rq')
    zh = request.GET.get('zh')
    rq2= request.GET.get('rq2')
    blx = request.GET.get('blx')
    #print type(rq),'11',type(blx),rq ,blx[0][0]   
    cursorsj = connection.cursor()
    sj1 = ''
    sj2=''
    sj3=''
    sj4=''
    sj5 = ''
    sj6 = ''
    sj7=''
    rqlist = ''
    zhlist=''
    if blx[0][0] =='1':#资产情况表
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct(rq) from njfx_zcqkb t ')
        rqlist = cursorrq.fetchall()
        if rq is None:
            rq = rqlist[0][0]
        cursorrq.close()
        cursorsj.execute('select rq, tzzhdm, zhmc, dwjz, stzcjz, zcfe, wtje, jsy, drrq from njfx_zcqkb where rq=%s order by rq desc ',[rq]) 
        sj1 = cursorsj.fetchall()       
    elif blx[0][0] =='2':# 归因分析
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct(jsrq) from NJFX_GYFX t order by jsrq desc')
        rqlist = cursorrq.fetchall()
        cursorrq.close()
        if rq is None:
            rq = rqlist[0][0]
        cursorsj.execute('select  ksrq, jsrq,zh, zclb, zcmc, sye1_bqlj, round(sye1_bqsyzb,2) ,sye1_bnlj, round(sye1_bnsyzb,2), sye2_bqlj, sye2_bnlj, round(tzsyl_bqlj,2), round(tzsyl_bnlj,2), drrq from njfx_gyfx where jsrq= %s order by jsrq desc',[rq])
        sj2 = cursorsj.fetchall()
    elif blx[0][0] =='3':#资产分布
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct(rq) from njfx_zcfbb t order by rq desc')
        rqlist = cursorrq.fetchall()
        cursorrq.close() 
        if rq is None:
            rq = rqlist[0][0]        
        cursorsj.execute('select  rq, zh, zclb, zcmc, sz, zjzcbl,  drrq from njfx_zcfbb where rq=%s order by rq desc',[rq])
        sj3 = cursorsj.fetchall()
    elif blx[0][0] =='4':#日均持仓分析
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct(jsrq) from njfx_zcfbbrjcc t order by jsrq desc')
        rqlist = cursorrq.fetchall()
        cursorrq.close() 
        if rq is None:
            rq = rqlist[0][0]            
        cursorsj.execute('select  ksrq, jsrq, zh, zclb, zcmc, rjcccb, rjccye, drrq from njfx_zcfbbrjcc order by jsrq desc')
        sj4 = cursorsj.fetchall()
    elif blx[0][0] =='5': #收入分析
        cursorsj.execute('select jsrq, zh, xm, zqnhg, qthbl, ldxxj, xyck, gz, qyz, kzz, llcp, qtgdl, gdlxj, gp, qtqyl, qylxj, hj from njfx_srfx order by jsrq desc ,zh,xm')
        sj5 = cursorsj.fetchall()
    elif blx[0][0] =='6': #投资分析
        print rq
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct(rq) from njfx_tzqkfx t ')
        rqlist = cursorrq.fetchall()
        if rq is None:
            rq = rqlist[0][0]
        cursorrq.close()
        cursorsj.execute('select rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr, bnlr, ljlr, sndwjz, sndtzhdwjz, sqdwjz, dwjz, bqjzzjbd, bnsyl, jz, ljpm, bnpm from njfx_tzqkfx t where t.rq= %s order by t.rq desc,t.id',[rq])
        sj6 = cursorsj.fetchall()
    elif blx[0][0] =='7': #每日资产净值
        cursorzhlist=connection.cursor()
        cursorzhlist.execute('select distinct zhsj from NJFX_NJZH t ')
        zhlist=cursorzhlist.fetchall()
        
        for x in zhlist:
            print x
        cursorzhlist.close() 
        print type(zhlist)
        if rq2 is None or rq is None or zh is None:
            cursorsj.execute('''select x.zhmc,x.rq, x.zh1zc, x.zh2zc, x.zh3zc, x.zh4zc,x.zhhj,x.tabd,x.tabdje,x.bdhzhhj,decode(y.zhhj,null,0,trunc(x.bdhzhhj/y.zhhj,4)) syl from njfx_syl x 
left join ( select a.id,a.zhmc,a.rq,lead(a.rq,1,0) over(order by a.rq) last_rq,a.zhhj as zhhj,a.bdhzhhj from NJFX_SYL a) y on y.zhmc=x.zhmc and x.rq=y.last_rq  where x.rq>=%s order by x.rq desc ''',[rq])
            print 'xxx'
        else:
            zhtemp ='%'+zh+'%'
            cursorsj.execute('''select x.zhmc,x.rq, x.zh1zc, x.zh2zc, x.zh3zc, x.zh4zc,x.zhhj,x.tabd,x.tabdje,x.bdhzhhj,decode(y.zhhj,null,0,trunc(x.bdhzhhj/y.zhhj,4)) syl from njfx_syl x 
left join ( select a.id,a.zhmc,a.rq,lead(a.rq,1,0) over(order by a.rq) last_rq,a.zhhj as zhhj,a.bdhzhhj from NJFX_SYL a) y on y.zhmc=x.zhmc and x.rq=y.last_rq where  x.zhmc like %s  and  x.rq>=%s  and x.rq<=%s order by x.rq desc''',[zhtemp,rq,rq2])
            print 'yyy'
        sj7 = cursorsj.fetchall()
        
    else:
        pass    
    cursorsj.close() 
    print rqlist
    return render_to_response('tghsj.html',{'sj1':sj1,'sj2':sj2,'rqlist':rqlist,'sj3':sj3,'sj4':sj4,'sj5':sj5,'sj6':sj6,'sj7':sj7,'blx':blx[0][0],'zhlist':zhlist,'kssj':rq,'jzsj':rq2,'zh':zh})
def Tzqkfx(request):
    cursorsj = connection.cursor()
    cursorsj.execute('''select distinct(t2.rq) from NJFX_gyfx t1,njfx_zcfbb t2,njfx_zcqkb t3 where t1.zh=t2.zh and t1.zh=t3.zhmc
and replace(replace(replace(t1.jsrq,'年','-'),'月','-'),'日','')= t2.rq and t2.rq=t3.rq''')
    rq = cursorsj.fetchall()
    rq1 = rq[0][0]
    cursorsj.close()
    #获取上期的日期，提醒防止数据计算错误
    cursorsqrq = connection.cursor()
    cursorsqrq.execute('select max(rq) from NJFX_TZQKFX t where zhmc=\'本期累计\'')
    sqrq = cursorsqrq.fetchall()
    sqrq = sqrq[0][0]
    #if sqrq:
        #print sqrq
        #sqrq = sqrq.strftime("%Y-%m-%d")
       #print type(sqrq),rq1,sqrq
    cursorsqrq.close()
    cursorsj.close()
    #先查出各项组合的明细分析数据
    sqldata =  '''select  rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr,'' as bnlr,ljlr,'' as sndwjz,'' as tzhsndwjz,sqdwjz,dwjz, ljpm,  bnpm from tzfx1_2 where rq= %s  
 union select  rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr,'' as bnlr,ljlr,'' as sndwjz,'' as tzhsndwjz,sqdwjz,dwjz,ljpm, 
 bnpm from tzfx2 where rq = %s   '''
    
    cursor = connection.cursor()
    cursor.execute(sqldata,[rq1,rq1])
    tzfx = cursor.fetchall()  
    cursor.close()     
    #各有效组合的总金额    
    return render_to_response('tzfx.html',{'rq':rq,'tzfx':tzfx,'sqrq':sqrq}) 
def save_tzqkfx(request):
    rq = request.POST.get('rq1') 
    # 先写入各组合明细
    sql1 = '''insert into njfx_tzqkfx ( rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr,ljlr,bnlr,sndwjz, sndtzhdwjz,sqdwjz,dwjz, bqjzzjbd,ljpm,  bnpm) '''
    sqldata1 =  '''select  rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj,sndljlr, ljlr, ljlr-sndljlr as bnlr,'' as sndwjz, '' as sndtzhdwjz,sqdwjz,dwjz,round(dwjz-sqdwjz,2) as bqjzzjbd, ljpm,  bnpm from tzfx1_2 where rq= %s  
               union select  rq,zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr,ljlr, ljlr-sndljlr as bnlr,'' as sndwjz, '' as sndtzhdwjz,sqdwjz,dwjz, round(dwjz-sqdwjz,2) as bqjzzjbd,ljpm,  bnpm from tzfx2 where rq = %s  '''
    sqldata2 = '''select  zhmc, wtje, yhck, zqnhg, qthbjj, hblxj, hblzb, hblsr, hblsrzb, xdg, wcp, qyz, qtgdl, gdlxj, gdlzb, gdlsr, gdlsrzb, gp, gpjj, qylxj, qylzb, gpzb, qylsr, qylsrzb, stzcjz, srhj, sndljlr, bnlr, ljlr, sndwjz, sndtzhdwjz, sqdwjz, dwjz, bqjzzjbd, bnsyl, jz, ljpm, 
 bnpm,rq from tzfxzjbd where rq = %s'''
    sqlinsert1  = sql1+sqldata1
    sqlinsert2  = sql1+sqldata2
    cursorsave = connection.cursor() # 清楚重复数据
    try:
        cursorsave.execute(sqlinsert1,[rq,rq]) 
        print 'ok'
    except Exception as error:
        print error
    try:
       # cursorsave.execute(sqlinsert2,[rq]) 
        print 'ok'
    except Exception as error:
        print error    
    cursorsave.close()                     
    return HttpResponseRedirect('/sjcx/?blx=6&rq='+rq)
def srfx(request):
    if request.method=="POST":
        rq1 = request.POST.get('rq1')
        print rq1
        cursorsrfxsave = connection.cursor()
        try:
            cursorsrfxsave.execute('insert into njfx_srfx (jsrq, zh, xm, zqnhg, qthbl, ldxxj, xyck, gz, qyz, kzz, llcp, qtgdl, gdlxj, gp, qtqyl, qylxj, hj) select jsrq, zh, xm, zqnhg, qthbl, ldxxj, xyck, gz, qyz, kzz, llcp, qtgdl, gdlxj, gp, qtqyl, qylxj, hj from srfx where jsrq= %s order by jsrq desc,zh,xm',[rq1])
        except:
            print ("fdsf")
        finally:
            cursorsrfxsave.close()
            return HttpResponseRedirect('/sjcx/?blx=5&rq='+rq1)
    else:
        cursorrq = connection.cursor()
        cursorrq.execute('select distinct jsrq from NJFX_ZCFBBRJCC t')
        rq = cursorrq.fetchall()
        cursorrq.close()
        rq1 = rq[0][0].encode("utf-8")  
        print type(rq1) 
        cursorsrfx = connection.cursor()
        cursorsrfx.execute('select jsrq, zh, xm, zqnhg, qthbl, ldxxj, xyck, gz, qyz, kzz, llcp, qtgdl, gdlxj, gp, qtqyl, qylxj, hj from srfx where jsrq= %s order by jsrq desc,zh,xm',[rq1])
        srfx = cursorsrfx.fetchall()
        cursorsrfx.close()         
        return render_to_response('srfx.html', {'srfx':srfx,'rq':rq})
def sylfx(request):
    if request.method=="POST":
        rq1 = request.POST.get('kssj')
        rq2 = request.POST.get('jzsj')
        rq1=str(rq1)
        rq2=str(rq2)
        print rq1,'||',rq2
        zh = request.POST.get('zh')
        zh1='成都路局-'+zh
        zh2='成都路局-'+zh+'2'
        zh3='成都路局-'+zh+'3'
        zh4='成都路局-'+zh+'4'
        syllist=[]
        cursorzhlist=connection.cursor()
        cursorzhlist.execute('select distinct zhsj from NJFX_NJZH t ')
        zhlist=cursorzhlist.fetchall()
        cursorzhlist.close()        
        print zh1
        cursortabd = connection.cursor()
        cursortabd.execute('''
        select  distinct(t1.rq),'%s' as zh,A.slje,B.slje,C.slje,D.slje,round(ifnull(A.slje,0)+ifnull(B.slje,0)+ifnull(C.slje,0)+ifnull(D.slje,0),2) as jehj,E.taslje,round(ifnull(A.slje,0)+ifnull(B.slje,0)+ifnull(C.slje,0)+ifnull(D.slje,0)+ifnull(E.taslje,0),2) as drje 
from njfx_zcjz t1 left join (select NJFX_ZCJZ.RQ,zh,NJFX_ZCJZ.SLJE as slje from NJFX_ZCJZ where zh='%s') A ON t1.rq=A.rq
left join (select NJFX_ZCJZ.RQ,zh,NJFX_ZCJZ.SLJE as slje from NJFX_ZCJZ where zh='%s') B ON t1.rq= B.rq
left join (select NJFX_ZCJZ.RQ,zh,NJFX_ZCJZ.SLJE as slje from NJFX_ZCJZ where zh='%s') C ON t1.rq=C.rq
left join (select NJFX_ZCJZ.RQ,zh,NJFX_ZCJZ.SLJE as slje from NJFX_ZCJZ where zh='%s') D ON t1.rq=D.rq
left join (select t.jzrq,sum(case when t.bz='申购款' then -(t.slje) else t.slje end) as  taslje from NJFX_TA t where zh like '%%%s%%' and  t.slje is not null   group by jzrq) E 
        on REPLACE(t1.RQ,'-','')=substr(e.jzrq,0,9) where t1.rq>='%s' and t1.rq<='%s' order by t1.rq
        ''' %(zh,zh1,zh2,zh3,zh4,zh1,rq1,rq2))
        tabd= cursortabd.fetchall()
        cursortabd.close() 
        for i in range(1,len(tabd)):
            bdtup = tabd[i]
            bdtuptmep = (round(tabd[i][8]/tabd[i-1][6], ndigits=4),)
            print bdtuptmep
            bdtup = bdtup+bdtuptmep
            
            syllist.append(bdtup)
        return render_to_response('sylfx.html', {'tabd':syllist,'zh':zhlist,'kssj1':rq1,'jzsj1':rq2,'zh1':zh})
    else:
        cursorzh=connection.cursor()
        cursorzh.execute('select distinct zhsj from NJFX_NJZH t ')
        zh=cursorzh.fetchall()
        cursorzh.close()
        return render_to_response('sylfx.html',{'zh':zh})
def sylfxsave(request):
    if request.method=="POST":
        rq1 = request.POST.get('kssj')
        rq2 = request.POST.get('jzsj')
        zh = request.POST.get('zh')
        rq1=str(rq1)
        rq2=str(rq2)
        #zh=zh.encode("utf-8")
        cursorzhlist=connection.cursor()
        cursorzhlist.execute('select distinct zhsj from NJFX_NJZH t ')
        zhlist=cursorzhlist.fetchall()
        cursorzhlist.close()        
        print type(rq1),rq1,zh
        cursortabd = connection.cursor()
        bdsql='select DISTINCT(X.RQ),\''+zh
        bdsql = bdsql+'''' AS zh,A.ZH1,B.ZH2,C.ZH3,D.ZH4,nvl(A.ZH1,0)+nvl(B.ZH2,0)+nvl(c.zh3,0)+nvl(d.zh4,0) AS JZHJ,E.SLJE AS BDJE,nvl(A.ZH1,0)+nvl(B.ZH2,0)+nvl(c.zh3,0)+nvl(d.zh4,0)+nvl(E.SLJE,0) AS DRJZ  from NJFX_ZCJZ x
left join (select NJFX_ZCJZ.RQ,'ss' AS zh,NJFX_ZCJZ.SLJE as zh1 from NJFX_ZCJZ WHERE ZH='''
        bdsql = bdsql + '\'成都路局-'+zh+'1\') A on X.RQ=A.RQ'
        bdsql = bdsql + ' left join (select NJFX_ZCJZ.RQ,\''+zh+'\' AS zh,NJFX_ZCJZ.SLJE as zh2 from NJFX_ZCJZ WHERE ZH=\'成都路局-'+zh+'2\') B on X.RQ=B.RQ'
        bdsql = bdsql + ' left join (select NJFX_ZCJZ.RQ,\''+zh+'\' AS zh,NJFX_ZCJZ.SLJE as zh3 from NJFX_ZCJZ WHERE ZH=\'成都路局-'+zh+'3\') C on X.RQ=C.RQ'
        bdsql = bdsql + ' left join (select NJFX_ZCJZ.RQ,\''+zh+'\' AS zh,NJFX_ZCJZ.SLJE as zh4 from NJFX_ZCJZ WHERE ZH=\'成都路局-'+zh+'4\') D on X.RQ=D.RQ'
        bdsql= bdsql + ' left join (select t.jzrq,sum(case when t.bz=\'申购款\' then -abs(t.slje) else t.slje end) as  slje from NJFX_TA t where zh like\'成都路局-'
        bdsql = bdsql+zh+'%\' and t.slje is not null   group by jzrq) E on REPLACE(x.RQ,\'-\',\'\')=TRUNC(e.JZRQ)  where x.rq>=\''+rq1+'\' and x.rq<=\''+rq2+'\' '
        insertsql = 'insert into njfx_syl (rq, zhmc, zh1zc, zh2zc, zh3zc, zh4zc,zhhj,  tabdje, bdhzhhj)' +bdsql
        delsql = 'delete from njfx_syl where zhmc like \''+zh+'\' and rq>=\''+rq1+'\' and rq<=\''+rq2+'\''
        print delsql
        try:
            cursortabd.execute(delsql) 
            print ('ok1ok1ok12')
        except Exception:
            print (Exception)
        try:
            cursortabd.execute(insertsql)
            print ('ok1ok1ok1')
        finally:
            cursortabd.close()
            return HttpResponseRedirect('/sjcx/?blx=7&rq='+rq1)
    