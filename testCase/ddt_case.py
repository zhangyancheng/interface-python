import unittest

import ddt

from Public.expect import assertre
from Public.get_excel import makedata
from Public.log import Log
from Public.select_request import TestApi

data_test = makedata()
logger = Log()

def my_print(msg):
    logger.info(msg)

@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        my_print('测试用例开始执行')

    def tearDown(self):
        my_print('测试用例执行完毕')

    @ddt.data(*data_test)
    def test_api(self, data_test):
        my_print('获取用例数据:%s' % data_test)
        api = TestApi(url=data_test['url'], key=data_test['key'], connent=data_test['coneent'], fangshi=data_test['fangshi'])
        my_print('输入参数：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['coneent'], data_test['fangshi']))
        apijson = dict(api.getJson())
        my_print('返回结果:%s' % apijson)
        qingwang=dict(assertre(asserqingwang=data_test['qiwang']))
        self.assertEqual(int(qingwang['code']), apijson['code'], msg='预期和返回不一致')
        my_print('断言结果:code预期值%s == 实际值%s' % (qingwang['code'], apijson['code']))

