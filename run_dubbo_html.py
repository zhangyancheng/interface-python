# -*- coding: utf-8 -*-
# @Author  : leizi
import datetime
import os
import time

from Public.get_excel import datacel
from Public.py_Html import createHtml
from branch.Dingtalk import send_ding
from testCase.dubbocase import testdubbointerface


def start_dubbo_case():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\test_case_data\\dubbocase.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testdubbointerface()
    filepath =os.path.join(basdir+'\\test_Report\\%s-result.html'%day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    createHtml(titles='dubbo接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    contec='dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s'%(list_pass,list_fail,list_exption,list_weizhi,filepath)
    send_ding(content=contec)
if __name__ == '__main__':
    start_dubbo_case()