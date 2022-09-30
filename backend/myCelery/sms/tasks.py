from myCelery.main import app

@app.task(name="send_sms")  # 通过装饰器让下方函数识别成任务
def send_sms():
    """发送邮箱验证码"""
    # 任务结果
    return "发送邮箱验证码"