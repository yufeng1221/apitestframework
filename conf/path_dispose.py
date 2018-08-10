import os
from conf.read_config import ReadConfig

#获取路径配置文件的绝对路径
conf_path = os.path.join(os.path.dirname(__file__),'path.conf')
conf_path = conf_path.replace('\\','/')


#获取项目路径
root_path = ReadConfig().read_config(conf_path,'ROOT_PATH','root_path')

#数据配置文件路径
auto_conf_path = os.path.join(os.path.dirname(__file__),'auto.conf')
auto_conf_path = auto_conf_path.replace('\\','/')#解决windous下的\问题

#根目录配置文件路径
root_conf_path = os.path.join(os.path.dirname(__file__),'path.conf')
root_conf_path = root_conf_path.replace('\\','/')

#数据库链接数据配置文件路径
db_liknde_path = os.path.join(os.path.dirname(__file__),'database.conf')
db_liknde_path = db_liknde_path.replace('\\','/')

#日志保存路径
log_path = os.path.join(root_path,'log_report','log')
log_path = log_path.replace('\\','/')

#测试报告保存路径
report_path = os.path.join(root_path,'log_report','report')
report_path = report_path.replace('\\','/')

#测试数据保存地址
test_data_path = os.path.join(root_path,'test_data','test_api_data.xlsx')
test_data_path = test_data_path.replace('\\','/')

#测试用例地址
test_case_path = os.path.join(root_path,'test_case','test_http_request.py')
test_case_path =test_case_path.replace('\\','/')