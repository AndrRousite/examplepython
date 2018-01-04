import time, math, smtplib,traceback
from email.mime.text import MIMEText
from email.utils import formataddr

print("hello index")

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b


def hello():
    print("hello function")


hello()

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# print(dir(math))
# print(dir(time))

# str = input("请输入：")
# print("您输入的内容为：", str)


file = open("./resource/README.md", "r+")

print("文件名称：", file.name, "\n是否关闭：", file.closed, "\n访问模式：", file.mode, "\n末尾是否强制加空格：")


file.close()


class User:
    def __init__(self):
        print("create")

    def __del__(self):
        print("destroy")


user = User()

print(user.__class__.__name__)

del user

my_sender = 'meiqi_uu@126.com'  # 发件人邮箱账号
my_pass = 'z15879418606'  # 发件人邮箱密码
my_user = 'w710989327@foxmail.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
