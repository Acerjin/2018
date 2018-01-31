# -*- coding: utf-8 -*-
import xlrd
def readexcel(startrow,startcol=0,*args,**kwargs):
    wb = xlrd.open_workbook(u'E:\\1.xls','r',formatting_info=True)
    ws  = wb.sheet_by_index(0)
    nrow = ws.nrows
    sqllist = []
    rowerrorlist = []
    for r in range(startrow,nrow):
        row_error=0
        for a in range(0,len(args)):
            if ws.row_values(r)[args[a]] =='':
                rowerrorlist.append(r)
                row_error = 1
                break
        if row_error ==0:
            sqllist.append(ws.row_values(r))
    for i in range(0,len(sqllist)):
        print i,':',sqllist[i],'||'
    for e in range(0,len(rowerrorlist)):
        print e,':',rowerrorlist[e],'||'
    print args,kwargs,kwargs['m']
readexcel(0,0,1,2,3,m=6)