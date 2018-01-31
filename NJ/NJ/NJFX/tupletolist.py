# -*- coding: utf-8 -*-
'''
Created on 2017

@author: Acerjin
'''
def dictfetchall(cursor):
    "测试"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]