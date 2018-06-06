# -*- coding: utf-8 -*-
from Public.requests import requ
from Public.log import Log
logger = Log()

def my_print(msg):
    logger.info(msg)

reques=requ()
class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi=='POST':
			self.parem = {'key': self.key, 'info': self.connent}
			self.response=reques.post(self.url,self.parem)
			my_print('成功发起POST请求，请求结果code为：:%s' % self.response)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.get(self.url,self.parem)
			my_print('成功发起GET请求，请求结果code为：:%s' % self.response)
		return self.response
	# def getJson(self):
	# 	json_data = self.testapi()
	# 	return json_data