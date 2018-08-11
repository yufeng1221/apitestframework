__author__ = 'zz'
import unittest

from ddt import ddt,data

from public.read_config import ReadConfig
from public.http_requests import HttpRequest
from public.do_excel import DoExcel
from public.my_log import MyLog
from conf import read_path
from public.do_mysql import DoMysql

#测试数据
ip=ReadConfig().read_config(read_path.config_path,'IP','ip')
mode=ReadConfig().read_config(read_path.config_path,'FLAG','mode')
case_id_list=ReadConfig().read_config(read_path.config_path,'FLAG','case_id_list')
test_data=DoExcel(read_path.test_data_path,'test_data',mode,case_id_list).do_excel()

#创建一个日志对象
logger=MyLog('python8')

#全局变量 COOKIES  可以用反射
COOKIES=None
REGTIME=None#注册时间
MEMBER_ID=None#用户id

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):#执行用例之前的准备工作
        logger.info("我要开始测试啦！")
        self.t=DoExcel(read_path.test_data_path,'test_data',mode,case_id_list)
        #保存测试结果的实例

    @data(*test_data)#拆分数据
    def test_api(self,item):#测试类里面的函数没有传参
        global COOKIES#声明全局变量
        global REGTIME#声明全局变量
        global MEMBER_ID#声明全局变量
        #执行http请求
        res=HttpRequest().http_request(ip+item['url'],eval(item['param']),item['method'],COOKIES)

        #每次请求之后就判断 是否产生COOKIES  如果产生 就替换全局变量
        #如果不产生 就不替换
        if res.cookies!={}:#就说该请求应该是登录请求 产生了cookie 类字典
            COOKIES=res.cookies
        #保存测试结果
        self.t.write_data(item['case_id']+1,8,str(res.json()))

        #替换REGTIME  查询注册时间
        if REGTIME==None:#regtime没有被替换的时候 我才去查询数据库
            query='select regtime from member where mobilephone=%s'
            query_condition=eval(item['param'])['mobilephone']
            result=DoMysql().do_mysql(query,(query_condition,),1)
            if result !=None:
                #查询结果不为空 以及REGTIME 没有被替换 我才去做替换？
                REGTIME=str(result[0])+'.0'

        #替换MEMBER_ID  查询用户id
        if MEMBER_ID==None:#member_id没有被替换的时候 我才去查询数据库
            query='select id from member where mobilephone=%s'
            query_condition=eval(item['param'])['mobilephone']
            result=DoMysql().do_mysql(query,(query_condition,),1)
            if result !=None:
                #查询结果不为空 以及MEMBER_ID 没有被替换 我才去做替换？
                MEMBER_ID=str(result[0])

        #首先判断我们的期望结果里面是否有 ${regtime} ${member_id}
        #此处是针对的充值的情况考虑
        if item['ExpectedResult'].find('${regtime}')!=-1:#替换regtime
            new_param=item['ExpectedResult'].replace('${regtime}',REGTIME)
            if new_param.find('${member_id}')!=-1:#替换member_id
                new_param=new_param.replace('${member_id}',MEMBER_ID)
                if new_param.find('${no_reg_tel}')!=-1:
                    new_param=new_param.replace('${no_reg_tel}',str(eval(item['param'])['mobilephone']))
        else:#如果没有找到需要替换的 就不做任何替换
            new_param=item['ExpectedResult']

        #执行sql语句的判断  当CheckSql不为空的时候 采取校验数据库
        if item['CheckSql']!=None:
            #检查数据里面是否有需要做替换的地方
            if item['CheckSql'].find('${no_reg_tel}')!=-1:
                sql_param=item['CheckSql'].replace('${no_reg_tel}',str(eval(item['param'])['mobilephone']))

            #替换完成之后要去做sql的查询
                query=eval(sql_param)['query']#查询语句
                query_condition=eval(sql_param)['query_condition']
                result=DoMysql().do_mysql(query,(query_condition,),1)
                try:
                    self.assertEqual(int(result[0]),int(eval(sql_param)['expected']))
                    sql_result='PASS'
                except AssertionError as e:
                    logger.error('数据库检查出错：{0}'.format(e))
                    sql_result='Fail'
                    raise e
                finally:
                    self.t.write_data(item['case_id']+1,10,sql_result)

        try:
            self.assertEqual(eval(new_param),res.json())#断言的作用？对比期望值与实际值
            test_result='PASS'
        except AssertionError as e:
            logger.error("执行用例的时候报错:{0}".format(e))
            test_result='FAIL'
            raise e#处理完异常之后  记得丢出去~异常不要留在家里
        finally:#不管怎样 都要写入结果值
            self.t.write_data(item['case_id']+1,9,test_result)#保存测试对比结果

    def tearDown(self):
        logger.info("我已经结束测试啦！")

