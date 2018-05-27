# -*- coding: utf-8 -*-
import xlrd
from Public.log import Log
from config import globalparam

log_path = globalparam.log_path
logger = Log()

def my_print(msg):
    logger.info(msg)

def datacel(filrpath):
    try:
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        listid = []
        listkey = []
        listconeent = []
        listurl = []
        listfangshi = []
        listqiwang = []
        listrelut = []
        listname = []
        for i in range(1, nrows):
            listid.append(me.cell(i, 0).value)
            listkey.append(me.cell(i, 2).value)
            listconeent.append(me.cell(i, 3).value)
            listurl.append(me.cell(i, 4).value)
            listname.append(me.cell(i, 1).value)
            listfangshi.append((me.cell(i,5).value))
            listqiwang.append((me.cell(i,6).value))
        return listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname
    except:
        my_print('打开测试用例失败，原因是:%s' % Exception)

def makedata():
    #import os
    #path = os.getcwd() + '\\test_case_data\\case.xlsx'
    path = globalparam.data_path + "./" + "case.xlsx"
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname=datacel(path)
    make_data = []
    try:
        for i in range(len(listid)):
            make_data.append({'url': listurl[i], 'key': listkey[i], 'coneent':listconeent[i],
                              'fangshi': listfangshi[i], 'qiwang': listqiwang[i]})
            i += 1
        return make_data
    except:
        my_print('打开测试用例失败，原因是:%s' % Exception)
