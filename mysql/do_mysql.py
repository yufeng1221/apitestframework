__author__ = 'zz'
import mysql.connector
from conf import read_path
from public.read_config import ReadConfig

class DoMysql:
    def __init__(self):
        self.config=eval(ReadConfig().read_config(read_path.config_path,'DB','config'))

    def do_mysql(self,query,query_condition,state):
        cnn=mysql.connector.connect(**self.config)
        cursor=cnn.cursor()
        cursor.execute(query,query_condition)
        if state==1:#表示只有一条数据
            result=cursor.fetchone()
        else:#否则有多条数据
            result=cursor.fetchall()
        cursor.close()
        cnn.close()
        return result

if __name__ == '__main__':
    query='select Leaveamount from member where mobilephone=%s'
    query_condition=('15080800042',)
    result=DoMysql().do_mysql(query,query_condition,state=1)
    print(result[0])#int(result[0])