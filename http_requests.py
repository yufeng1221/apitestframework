import requests

class HttpRequest:
    def http_request(self,url,param,method):
        if method.lower() == 'get':
            try:
                res = requests.get(url,param)
                print('post请求响应结果：', res.status_code, res.json()['msg'])
            except Exception as e:
                print('请求出错:{0}'.format(e))

        elif method.lower() == 'post':
             try:
                res = requests.post(url,param)
                print('get请求响应结果：', res.status_code, res.json()['msg'])
             except Exception as e:
                print('请求出错:{0}'.format(e))
        else:
            print('请求错误！')
        return res.json()


