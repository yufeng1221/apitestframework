import configparser#专门读取配置文件的类

#打开文件
class ReadConfig:
    def read_config(self,conf_file,section,option):
        cf=configparser.ConfigParser()
        cf.read(conf_file,encoding='utf-8')
        value=cf.get(section,option)#section 片段 option 选项 value 值
        return value

if __name__ == '__main__':
   value=ReadConfig().read_config('auto.conf','IP','ip')
   print(value)