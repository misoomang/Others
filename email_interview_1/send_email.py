#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email_interview_1 import conf


def read_receiver():
    email_list = []
    with open(os.path.join(os.path.dirname(__file__), 'email_list.txt'), 'r') as f:
        for line in f.readlines():
            email_list.append(line)
    return email_list


def get_resume_path():
    return os.path.join(os.path.dirname(__file__), conf.MY_RESUME)


def email_send(send_emails, *args, **kwargs):
    # try:
    my_email = conf.MY_EMAIL
    my_pass = conf.MY_PASS
    my_name = conf.MY_NAME
    text = conf.MY_TEXT
    domain = conf.SERVER_DOMAIN
    port = conf.SERVER_PORT
    server = smtplib.SMTP_SSL(domain, port)
    server.login(my_email, my_pass)
    try:
        for send_email in send_emails:
            message = MIMEMultipart()
            msg = MIMEText(text, 'html', 'utf-8')                                   # 正文内容（html）
            message.attach(msg)
            message['From'] = formataddr([my_name, my_email])                         # 发送方
            message['To'] = formataddr(['尊敬的hr', send_email])                    # 收件方
            message['Subject'] = 'xxxx'                                             # 标题

            # 增加简历附件
            att1 = MIMEApplication(open(get_resume_path(), 'rb').read())
            att1["Content-Type"] = 'application/octet-stream'
            att1.add_header('Content-Disposition', 'attachment', filename=conf.MY_RESUME)
            message.attach(att1)

            server.sendmail(my_email, [send_email, ], message.as_string())
            print('%s 发送成功', send_email)
            time.sleep(15)
        # except Exception as e:
        #     print('发送失败', e)
    except Exception as e:
        print(e)
    finally:
        server.quit()


if __name__ == '__main__':
    receiver = read_receiver()
    email_send(receiver)
