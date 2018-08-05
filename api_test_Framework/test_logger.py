__author__ = 'Administrator'
import logging
import time


class TestLogger:

    def __init__(self,name):
        self.name = name
        # 创建日志接收
        self.logger = logging.getLogger(self.name)

    def test_logger(self,msg,level):
        # 设置接收的日志级别
        self.logger.setLevel('DEBUG')

        #格式化输出
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #输出日志到控制台
        output_console = logging.StreamHandler()
        output_console.setLevel('DEBUG')
        output_console.setFormatter(formatter)

        #输出日志到文本文件
        current_date = time.strftime('%Y-%m-%d')#当前日期
        file_neme = 'API_test_logger_'+current_date+'.txt'#文档名称
        output_text = logging.FileHandler(file_neme,encoding='UTF-8')
        output_text.setLevel('DEBUG')
        output_text.setFormatter(formatter)

        #输出与接收器对接
        self.logger.addHandler(output_console)
        self.logger.addHandler(output_text)

        #优化日志接收方法
        if level ==  'DEBUG':
            self.logger.debug(msg)
        elif level == 'INFO':
            self.logger.info(msg)
        elif level == 'WARNING':
            self.logger.warning(msg)
        elif level == 'ERROR':
            self.logger.error(msg)
        elif level == 'CRITICAL':
            self.logger.critical(msg)
        #处理日志重复打印的问题
        #每次输出日之后清除Handler
        self.logger.removeHandler(output_console)
        self.logger.removeHandler(output_text)

    def debug(self,msg = None):
        self.test_logger(msg,'DEBUG')

    def info(self,msg):
        self.test_logger(msg,'INFO')

    def warning(self,msg):
        self.test_logger(msg,'WARNING')

    def error(self,msg):
        self.test_logger(msg,'ERROR')

    def critical(self,msg):
        self.test_logger(msg,'CRITICAL')

