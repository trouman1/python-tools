# smtplib模块主要用于处理SMTP协议,email模块主要处理邮件的头和正文等数据
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:

    def __init__(self, user='1561140854@qq.com', password='gjiunsfxtumkjjhb'):
        print('登陆中…')
        # 建立与邮件服务器的连接
        self.conn = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 如果是ssl的话用 .SMTP_SSL
        self.conn.login(user=user, password=password)  # 登录

    def __del__(self):
        self.conn.close()
        print('已登出！')

    def send(self, sender='1561140854@qq.com', receiver='ryqsfx@163.com', subject='这是个主题', text='这是正文'):  # 发送邮件
        # 构建邮件的主体对象
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        body = text
        content = MIMEText(body, 'html', 'utf-8')
        msg.attach(content)  # 添加到msg
        # 添加邮件附件
        attachment = MIMEApplication(open(r'E:\素材\1.webp', 'rb').read())
        filename = '1.webp'
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)  # 添加到msg
        try:
            self.conn.sendmail(sender, receiver, str(msg))  # 发送
            print('邮件发送成功！！！')
        except:
            print('邮件发送失败！！！')


if __name__ == '__main__':
    s = SendEmail()  # 默认登录 user= password=
    s.send(subject='你好世界', text='halo world')  # sender= 与receiver= 同样可以自定义
