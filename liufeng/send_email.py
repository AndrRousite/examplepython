#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/8 16:11
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from venv import logger

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

__send_email__ = 'meiqi_uu@126.com'

ret = True
try:
    msg = MIMEText("hello ,send by Python...", 'plain', 'utf-8')

    msg['From'] = formataddr(['zhangsan', __send_email__])
    msg['To'] = formataddr(['liufeng', __email__])
    msg['Subject'] = "hello ,liufeng"

    server = smtplib.SMTP_SSL('smtp.126.com', 465)

    server.login(__send_email__, input("请输入您的邮箱密码: "))
    server.sendmail(__send_email__, (__email__,), msg.as_string())
    server.quit()
except Exception as e:
    logger.error(e)
    ret = False


if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

