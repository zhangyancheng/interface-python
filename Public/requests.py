# -*- coding: utf-8 -*-import requests,jsonfrom Public.log import Logfrom xml.etree.ElementTree import Elementfrom xml.etree.ElementTree import tostringimport xml.etree.ElementTree as ETlogger = Log()def my_print(msg):    logger.info(msg)class requ():    def __init__(self):        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}    def dict_to_xml(self,tag,d):        #tag为头尾标签，d传入字典        elem = Element(tag)        for key, val in d.items():            child = Element(key)            child.text = str(val)            elem.append(child)        return elem    def xml_to_dict(self,xml_str):        msg = {}        root_elem = ET.fromstring(xml_str)        for ch in root_elem:            msg[ch.tag] = ch.text        return msg    def get(self, url,params):#get消息        try:            r = requests.get(url, params=params, headers=self.headers)            r.encoding = 'UTF-8'            json_response = r.status_code            #json_response = r.status_code            return json_response            #return {'code': 0, 'result': json_response}        except Exception as e:            my_print('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}    def post(self, url, params):#post消息        data = json.dumps(params)        try:            r =requests.post(url,params=data,headers=self.headers)            json_response = json.loads(r.text)            #return {'code': 0, 'result': json_response}            return json_response        except Exception as e:            my_print('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}    def delfile(self,url,params):#删除的请求        try:            del_word = requests.delete(url,params=params, headers=self.headers)            json_response = json.loads(del_word.text)            return {'code': 0, 'result': json_response}        except Exception as e:            my_print('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}    def putfile(self,url,params):#put请求        try:            data = json.dumps(params)            me = requests.put(url, data)            json_response = json.loads(me.text)            return {'code': 0, 'result': json_response}        except Exception as e:            my_print('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}