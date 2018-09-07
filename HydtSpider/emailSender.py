# 添加文件 emailSender.py
import smtplib
import datetime
from email.mime.text import MIMEText


class emailSender(object):
    def __init__(self):
        self.smtp_host = "smtp.qq.com"      # 发送邮件的smtp服务器（从QQ邮箱中取得）
        self.smtp_user = "1152684231@qq.com"  # 用于登录smtp服务器的用户名，也就是发送者的邮箱
        self.smtp_pwd = "anzjdhlfuqzdhfce"  # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
        self.smtp_port = 465                # smtp服务器SSL端口号，默认是465
        self.sender = "1152684231@qq.com"    # 发送方的邮箱

    def sendEmail(self, toLst, subject, body):
        '''
        发送邮件
        :param toLst: 收件人的邮箱列表["1152684231@qq.com", "1785381349@qq.com"]
        :param subject: 邮件标题
        :param body: 邮件内容
        :return:
        '''
        message = MIMEText(body, 'plain', 'utf-8')  # 邮件内容，格式，编码
        message['From'] = self.sender               # 发件人
        message['To'] = ",".join(toLst)             # 收件人列表
        message['Subject'] = subject                # 邮件标题
        try:
            smtpSSLClient = smtplib.SMTP_SSL(
                self.smtp_host, self.smtp_port)   # 实例化一个SMTP_SSL对象
            loginRes = smtpSSLClient.login(
                self.smtp_user, self.smtp_pwd)      # 登录smtp服务器
            # loginRes = (235, b'Authentication successful')
            print(f"登录结果：loginRes = {loginRes}")
            if loginRes and loginRes[0] == 235:
                print(f"登录成功，code = {loginRes[0]}")
                smtpSSLClient.sendmail(self.sender, toLst, message.as_string())
                print(
                    f"mail has been send successfully. message:{message.as_string()}")
            else:
                print(f"登陆失败，code = {loginRes[0]}")
        except Exception as e:
            print(f"发送失败，Exception: e={e}")
