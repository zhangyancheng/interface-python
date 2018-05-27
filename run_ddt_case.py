import os
import time
import unittest
from branch import BSTestRunner
from config import globalparam
from testcase.ddt_case import MyTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'test_Report')
    filename = globalparam.report_path + "\\" + now + "result.html"
    re_open = open(filename, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='http接口测试报告', description='测试结果')
    m=runner.run(suite)
    #contec = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，未知错误：%s,详情见：%s' % (m.success_count,m.failure_count, m.error_count,file)
    #send_ding(content=contec)