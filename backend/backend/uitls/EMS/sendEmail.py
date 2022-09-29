from smtplib import SMTP_SSL
from email.mime.text import MIMEText

def sendMailCode(message, Subject, sender_show, recipient_show, to_addrs, cc_show=""):
    """
    :parms message: str 邮件内容
    :parms Subject: str 邮件主题描述
    :parms sender_show: str 发件人显示，不起实际作用，如：“xxx”
    :parms recipient_show: str 收件人显示，不起实际作用，多个收件人用','分隔开，如：“xxx， xxx”
    :parms to_addrs: str 实际收件人
    :parms cc_show: str 抄收人显示，不起实际作用，多个抄收人用','分隔开，如：“xxx， xxx”
    """

    # 填写真实的发邮件服务器用户名，密码
    user = '2945002921@qq.com'
    password = "wsuzkmoqrjffdcha"
    # 邮件内容
    msg = MIMEText(message, "plain", _charset="utf-8")
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["From"] = sender_show
    # 收件人显示，不起实际作用
    msg["To"] = recipient_show
    # 收件人显示，不起实际作用
    msg["Cc"] = cc_show
    with SMTP_SSL(host="smtp.qq.com", port=465) as smtp:
        # 登录发邮件服务器
        smtp.login(user = user, password = password)
        # 实际发送，接收邮件配置
        smtp.sendmail(from_addr = user, to_addrs = to_addrs, msg=msg.as_string())