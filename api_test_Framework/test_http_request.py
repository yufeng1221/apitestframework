import unittest
from ddt import ddt,data
from api_test_Framework.read_config import ReadConfig
from api_test_Framework.http_requests import HttpRequest
from api_test_Framework.do_excel import DoExcel
from api_test_Framework.test_logger import TestLogger

#测试数据
ip=ReadConfig().read_config('auto.conf','IP','ip')
mode=ReadConfig().read_config('auto.conf','FLAG','mode')
case_id_list=ReadConfig().read_config('auto.conf','FLAG','case_id_list')
test_data=DoExcel('test_api_data.xlsx','test_data','init_data',mode,case_id_list).do_excel()

#日志收集器
logger = TestLogger('test')

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):#执行用例之前的准备工作
        logger.debug("用例开始执行！")
        self.t=DoExcel('test_api_data.xlsx','test_data','init_data',mode,case_id_list)
        #保存测试结果的实例

    @data(*test_data)#拆分数据
    def test_api(self,item):#测试类里面的函数没有传参s%s%s
        #执行http请求
        logger.info('%s%s%s'%(ip+item['url'],eval(item['param']),item['method']))
        res=HttpRequest().http_request(ip+item['url'],eval(item['param']),item['method'])
        #保存测试结果
        self.t.write_data(item['case_id']+1,7,str(res))
        try:
            logger.info('预期结果：%s实际结果：%s'%(eval(item['ExpectedResult']),res))
            self.assertEqual(eval(item['ExpectedResult']),res)#断言的作用？对比期望值与实际值
            test_result='PASS'
            logger.debug('测试用例是否通过：通过')
        except AssertionError as e:
            logger.error("执行用例的时候报错:{0}".format(e))
            test_result='FAIL'
            logger.debug('测试用例是否通过：未通过')
            raise e#抛出异常
        finally:#有无问题都写入结果
            self.t.write_data(item['case_id']+1,8,test_result)#保存测试对比结果

    def tearDown(self):
        logger.debug("用例测试结束！")

