import requests
from log_report.test_logger import TestLogger

#日志收集
logger = TestLogger('test')


class HttpRequest:

    def http_request(self,url,param,method,cookie):
        if method.lower() == 'get':
            try:
                logger.info('请求参数 url：%s 账号信息：%s cookies：%s' %(url,param,cookie))
                res = requests.post(url,param,cookies=cookie)
                logger.debug('post请求响应结果：%s'%res.json())
                return res
            except Exception as e:
                logger.error('请求出错:{0}'.format(e))

        elif method.lower() == 'post':
             try:
                logger.info('请求参数 url：%s 账号信息：%s cookies：%s' %(url,param,cookie))
                res = requests.get(url,param,cookies=cookie)
                logger.debug('get请求响应结果：%s'%res.json())
                return res
             except Exception as e:
                logger.error('请求出错:{0}'.format(e))
        else:
            logger.error('请求错误！')


if __name__ == '__main__':
    log_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    log_parameter = {"mobilephone": "13548773642", "pwd": "123456"}
    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    recharge_parameter = {"mobilephone": "13548773642", "amount": "100"}
    hr = HttpRequest()
    hr.http_request(log_url, log_parameter, method='post')
    hr.http_request(recharge_url, recharge_parameter, method='get')