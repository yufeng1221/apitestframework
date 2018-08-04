__author__ = 'Administrator'
import logging
import time


class TestLogger:

    def __init__(self,name):
        self.name = name


    def test_logger(self,msg,level):
        #创建日志接收
        logger = logging.getLogger(self.name)
        logger.setLevel('DEBUG')#设置接收的日志级别

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
        logger.addHandler(output_console)
        logger.addHandler(output_text)
        #处理日志重复打印的问题
        #每次输出日之后关闭
        logger.removeHandler(output_console)
        logger.removeHandler(output_text)

        #优化日志接收方法
        if level ==  'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)

    def debug(self,msg):
        self.test_logger(msg,'DEBUG')

    def info(self,msg):
        self.test_logger(msg,'INFO')

    def warning(self,msg):
        self.test_logger(msg,'WARNING')

    def error(self,msg):
        self.test_logger(msg,'ERROR')

    def critical(self,msg):
        self.test_logger(msg,'CRITICAL')
