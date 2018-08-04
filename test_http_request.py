import unittest
from ddt import ddt,data
from api_test_Framework.read_config import ReadConfig
from api_test_Framework.http_requests import HttpRequest
from api_test_Framework.do_excel import DoExcel

#测试数据
ip=ReadConfig().read_config('auto.conf','IP','ip')
mode=ReadConfig().read_config('auto.conf','FLAG','mode')
case_id_list=ReadConfig().read_config('auto.conf','FLAG','case_id_list')
test_data=DoExcel('test_api_data.xlsx','test_data','init_data',mode,case_id_list).do_excel()

#日志收集器

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):#执行用例之前的准备工作
        print("用例开始执行！")
        self.t=DoExcel('test_api_data.xlsx','test_data','init_data',mode,case_id_list)
        #保存测试结果的实例

    @data(*test_data)#拆分数据
    def test_api(self,item):#测试类里面的函数没有传参
        #执行http请求
        res=HttpRequest().http_request(ip+item['url'],eval(item['param']),item['method'])
        #保存测试结果
        self.t.write_data(item['case_id']+1,7,str(res))
        try:
            self.assertEqual(eval(item['ExpectedResult']),res)#断言的作用？对比期望值与实际值
            test_result='PASS'
        except AssertionError as e:
            print("执行用例的时候报错:{0}".format(e))
            test_result='FAIL'
            raise e#抛出异常
        finally:#有无问题都写入结果
            self.t.write_data(item['case_id']+1,8,test_result)#保存测试对比结果

    def tearDown(self):
        print("用例测试结束！")

