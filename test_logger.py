__author__ = 'Administrator'
import logging
import time

class TestLogger:
    def test_logger(self):
        #创建日志接收
        logger = logging.getLogger('test')
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
        logger.removeHandler(output_console)
        logger.removeHandler(output_text)


        #优化日志接收方
11111
