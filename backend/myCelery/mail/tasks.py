from myCelery.main import app
from backend.uitls.EMS import sendEmail

@app.task(name="send_email")  # 通过装饰器让下方函数识别成任务
def send_email(email, sms_code):
    """发送邮箱验证码"""
    # 任务结果
    sendEmail.sendMailCode(message="您正在申请发送验证码：为了账号安全，请在指定位置输入下列验证码：{} 。 验证码涉及个人账号隐私安全，切勿向他人透漏。".format(sms_code)
                           , Subject="可容书阁验证码邮件"
                           , sender_show="可容书阁"
                           , recipient_show=email
                           , to_addrs=email)