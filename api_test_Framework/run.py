import time
import unittest
import HTMLTestRunnerNew
from api_test_Framework.send_email import EMail
from api_test_Framework.read_config import ReadConfig

class run:
    def run_test_case(self):
        suite=unittest.TestSuite()#创建测试套件
        suite.addTest(unittest.TestLoader().loadTestsFromName('test_http_request.TestHttpRequest'))#加载用例
        print(suite)

        with open("api_测试报告.html","wb+") as file:#执行用例并生成测试报告
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='api_测试报告.html',description='6666',tester='语枫')
            runner.run(suite)
        self.send_email()

    def send_email(self):
        email_data = ReadConfig().read_config('auto.conf', 'EMAIL', 'email_data')
        send_resser = eval(email_data)[0]
        send_resser_pasaword = eval(email_data)[1]
        receive_ressee = eval(email_data)[2]
        text_part = eval(email_data)[3]
        run_send = EMail(send_resser,send_resser_pasaword,receive_ressee,text_part)
        run_send.send_email()

if __name__ == '__main__':
    run_test = run()
    run_test.run_test_case()
