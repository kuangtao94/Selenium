import smtplib
import os
from email.mime.multipart import MIMEMultipart #邮件附件类
from email.mime.text import MIMEText #邮件模板类
from email.header import Header #邮件头部模板

#发送带附件的函数
def semd_mail(file_new):
    with open(file_new, "rb") as fp:
        mail_body = fp.read()

    #基本信息
    smtpserver = "smtp.163.com"
    port = 25
    sender = "18797815816@163.com"
    psw = "qqq123..." #163邮箱密码
    receiver = "1512500241@qq.com"

    #定义邮箱主题
    msg = MIMEMultipart()
    msg['subject'] = Header(u"自动化测试报告","utf-8")
    msg['from'] = sender
    msg["to"] = receiver

    #不加msg['from'] msg["to"]会报错,是因为"收件人和发件人没有定义"
    #HTML 邮件正文,直接发送附件的代码
    body = MIMEText(mail_body,"html","utf-8")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html'
    msg.attach(att)

    #链接邮件服务器发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    print("邮件发送成功")
    smtp.quit()


#查找最新的邮件
def new_file(report_path):
    result_path = report_path
    lists = os.listdir(result_path)
    lists.sort() #从小到大排序
    file = [x for x in lists if x.endswith(".html")]
    file_new_name = os.path.join(result_path,file[-1])
    return file_new_name