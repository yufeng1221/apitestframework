
import smtplib#构造登陆
from email.mime.text import MIMEText#构造正文内容
from email.mime.multipart import MIMEMultipart
class EMail:
    def __init__(self,send_resser,send_resser_pasaword,receive_ressee,text_part,enclosure):
        self.send_resser = send_resser
        self.send_resser_pasaword = send_resser_pasaword
        self.receive_ressee = receive_ressee
        self.text_part = text_part
        self.enclosure = enclosure

    def send_email(self):
        msg=MIMEMultipart()
        msg['Subject'] = '语枫的测试报告'
        msg['From'] = self.send_resser
        msg['To'] = self.receive_ressee
        #正文
        msg_1=MIMEText(self.text_part)
        msg.attach(msg_1)#将正文添加到邮件
        #附件
        msg_2=MIMEText(open(self.enclosure,'rb').read(),'html','utf-8')
        msg_2.add_header('Content-Disposition', 'attachment',filename=self.enclosure)
        msg.attach(msg_2)
        #登录信息
        s=smtplib.SMTP_SSL('smtp.qq.com')
        s.login(self.send_resser,self.send_resser_pasaword)#授权码
        s.sendmail(self.send_resser,self.receive_ressee,msg.as_string())
        s.close()

if __name__ == '__main__':
    send_resser = '252039429@qq.com'
    send_resser_pasaword = 'jnqzqqifobgzbhgj'
    receive_ressee = '252039429@qq.com'
    text_part = 'hello，华佬，这是语枫的测试报告'
    enclosure ='api_test_0731.html'
    run_send = EMail(send_resser,send_resser_pasaword,receive_ressee,text_part,enclosure)
    run_send.send_email()