from flask import Flask
from flask_cors import CORS
from flask import request
import json
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/send' ,methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        data = request.data.decode("utf-8")
        datas = json.loads(data)
        send(datas)

        return "成功"

def send(datas):
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"        # 设置服务器
    mail_user = "bzqjames@163.com"    # 用户名
    mail_pass = "bzq3511685"          # 口令
    sender = 'bzqjames@163.com'
    receivers = ['bzqweiyi@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    name = datas.get("name", "")
    mail = datas.get("mail", "")
    phone = datas.get("phone", "")
    subject = datas.get("subject", "")
    content = "姓名：" + name + " 邮箱：" + mail + " 电话：" + phone + " 主题："+subject
    title = name + '：联系了采金数据' # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)