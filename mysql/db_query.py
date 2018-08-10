import mysql.connector
from conf.read_config import ReadConfig
from conf.path_dispose import db_liknde_path
class DB_Query:

    def __init__(self,operation,param,multiline):
        self.operation = operation
        self.param = param
        self.multiline= multiline

    def db_query(self):
        db_linked_data = eval(ReadConfig().read_config(db_liknde_path,'MYSQL','linked_data'))
        #创建数据库连接
        db_linked = mysql.connector.connect(**db_linked_data)
        #创建游标
        cursor = db_linked.cursor()
        #操作数据库
        cursor.execute(self.operation,self.param)
        # 创建数据接收
        #判断是否多行显示
        if  self.multiline == '0':#0展示所有数据
            result = cursor.fetchall()
            print(result)
        elif self.multiline == '1':#1展示一条数据
            result = cursor.fetchone()
            print(result)
        #涉及到更新数据库数据是操作提交
        cursor.execute('commit')






if __name__ == '__main__':
    select = "select * from cu_customer where customer_id=%s"
    param = '2325a7afcadb4cb2a21ddb1c1a4b5523'
    a = DB_Query(select,(param,),multiline = '1')
    a.db_query()