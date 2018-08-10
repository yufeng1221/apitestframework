import os,time
import unittest
import HTMLTestRunnerNew
from e_mail.send_email import EMail
from conf.read_config import ReadConfig
from conf.path_dispose import report_path,auto_conf_path,test_case_path

class run:
    def run_test_case(self):
        suite=unittest.TestSuite()#创建测试套件
        suite.addTest(unittest.TestLoader().loadTestsFromName('test_case.test_http_request'))#加载用例
        print(suite)

        #测试报告保存地址拼接
        report_generate_time = time.strftime('%Y-%m-%d_%H')
        report_name = 'api_测试报告'+report_generate_time+'.html'
        report_seva_path = os.path.join(report_path,report_name)
        report_seva_path = report_seva_path.replace('\\', '/')
        with open(report_seva_path,"wb+") as file:#执行用例并生成测试报告
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title=report_name,description='6666',tester='语枫')
            runner.run(suite)
        #self.send_email()

    def send_email(self):
        email_data = ReadConfig().read_config(auto_conf_path, 'EMAIL', 'email_data')
        send_resser = eval(email_data)[0]
        send_resser_pasaword = eval(email_data)[1]
        receive_ressee = eval(email_data)[2]
        text_part = eval(email_data)[3]
        run_send = EMail(send_resser,send_resser_pasaword,receive_ressee,text_part)
        run_send.send_email()

if __name__ == '__main__':
    run_test = run()
    run_test.run_test_case()
