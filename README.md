# interface-python
#### 一、实现方法
1.通过python+flask编写Restful API，不再去依赖其他接口写自动化，实现自给自足<br>
<br>
2.运行Restful_Api下的api.py，可先通过postman或其他接口工具自测接口是否运行正常<br>
<br>
3.使用python+requests请求接口<br>
<br>
4.这里使用ddt数据驱动读取Excel中的测试用例执行<br>
<br>
5.输出测试报告和日志<br>

#### 二、框架目录的讲解<br>
![no view](https://github.com/zhangmoumou1/interface-python/blob/master/readme/%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg)<br>
<br>
1.Public和branch文件夹主要写一些公共、处理方法,如请求的二次封装、获取Excel数据、日志输出、测试报告优化,配置文件读取等;<br>
<br>
2.Restful_Api文件夹为接口的实现，运行api.py,通过postman请求验证;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface-python/blob/master/readme/postman.jpg)<br>
<br>
3.config文件夹用例管理路径,config.ini为项目的主路径,globalparam.py为日志文件、测试用例读取和存储的路径;<br>
<br>
4.report文件夹下存放日志和测试报告;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface-python/blob/master/readme/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.jpg)<br>
<br>
![no view](https://github.com/zhangmoumou1/interface-python/blob/master/readme/%E6%97%A5%E5%BF%97.jpg)<br>
<br>
5.testCase文件夹写了测试用例,通过ddt数据驱动读取Excel文件,用unittest单元测试框架管理用例;<br>
<br>
6.testdata文件下是测试用例;<br>
<br>
7.运行run_ddt_case.py执行用例(如果整个调用流程不太懂的可以看readme下的xmind流程图)。