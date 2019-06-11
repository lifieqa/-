#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/28

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.text import MIMEText
import unittest
import time
import os
import HTMLTestRunner
from email.mime.multipart import MIMEMultipart


# 定义发送邮件
def send_mail(file_new):
    '''发送邮件'''
    f = open(file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    smtp = smtplib.SMTP('smtp.sina.com')
    sender = 'lifeiqa@sina.com'

    password = 'lifei123456'
    receiver = '3039126375@qq.com'
    smtp.login(sender, password)
    msg = MIMEMultipart()
    # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    # 发送正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    # 定义邮件正文标题
    text['Subject'] = Header('接口自动化测试报告', 'utf-8')
    msg.attach(text)
    # 发送附件
    # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
    msg['Subject'] = Header('好店长测试报告' + getNowtime(), 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_file)
    # 定义发件人，如果不写，发件人为空
    msg['From'] = sender
    # 定义收件人，如果不写，收件人为空
    # msg['To'] = ",".join(receiver)
    msg['To'] = receiver
    tmp = smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def reportmulu():
    '''获取report的目录'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report')


def new_report(testreport):
    '''查找测试报告目录，找到最新生成的测试报告文件'''
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new


def getSuite():
    '''获取测试套件'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests'),
        pattern='test_*.py',
        top_level_dir=None)
    return suite


def getNowtime():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


# if __name__ == '__main__':
#     fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report', getNowtime() + 'testReport.html')
#     HTMLTestRunner.HTMLTestRunner(stream=open(fp, 'wb'),
#                                   title='自动化测试报告',
#                                   description='自动化测试报告详细信息').run(getSuite())
#
#     new_file = new_report(reportmulu())
#     send_mail(new_file)

if __name__ == '__main__':
    suite=getSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)
    # print(getSuite())

# print(new_report(reportmulu()))
