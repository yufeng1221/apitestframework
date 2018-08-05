import requests
from api_test_Framework.test_logger import TestLogger

logger = TestLogger('test')

class HttpRequest:
    def http_request(self,url,param,method):
        if method.lower() == 'get':
            try:
                logger.info('请求参数：%s%s' % (url, param))
                res = requests.post(url,param)
                logger.debug('post请求响应结果：%s'%res.json())
            except Exception as e:
                logger.error('请求出错:{0}'.format(e))

        elif method.lower() == 'post':
             try:
                logger.info('请求参数：%s%s'%(url,param))
                res = requests.get(url,param)
                logger.debug('get请求响应结果：%s'%res.json())
             except Exception as e:
                logger.error('请求出错:{0}'.format(e))
        else:
            logger.error('请求错误！')
        return res.json()

