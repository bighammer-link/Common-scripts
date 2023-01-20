'''
这是一个可以获取当天天气状况并且推送到微信或者是QQ邮箱的脚本。里面涉及到和风天气API（https://www.qweather.com/）的注册，真不知道怎么注册的话，
详细步骤请到：https://blog.csdn.net/qq_51208442/article/details/128709186?spm=1001.2014.3001.5501查看

'''
# -*- coding: utf8 -*-
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 修改为自己的和风天气的KEY
KEY = ''

# 这里是想要查看天气的地方的经纬度(经度纬度之间使用英文逗号隔开，最多保留两位小数)
location = ''

# 这里使用的是server的推送方式，如果使用邮箱推送请忽略
SCKEY = ''

# 这里是QQ邮箱推送
# 这是发件人
from_mail = ''

# 这是收件人,多个的话请用英文逗号隔开
to_mial = ''

# 发件人的邮箱授权码（可自行百度如何获取）
right_code = ''
# --------------------------------------------------------------分割线---------------------------------------------------------------
weather_url = 'https://devapi.qweather.com/v7/weather/3d?location={}&key={}'.format(location, KEY)
weather_html = requests.get(weather_url).json()
info = weather_html["daily"]

# 获取当天天气
data, data1 = info[0]['fxDate'], info[1]['fxDate']
tempMax, tempMax1 = info[0]['tempMax'], info[1]['tempMax']
tempMin, tempMin1 = info[0]['tempMin'], info[1]['tempMin']
textDay, textDay1 = info[0]['textDay'], info[1]['textDay']
textNight, textNight1 = info[0]['textNight'], info[1]['textNight']

# 编辑要发送的内容
title = '今日份天气已到账'
desp = '今日：{}\n\n今天最高气温：{}℃\n\n今天最低气温：{}℃\n\n今天白天天气：{}\n\n今天夜间天气：{}\n\n注意穿衣！\
    又是未来可期的一天！\n\n\n\n\n\n\n\n下面是明天的天气\n\n明天：{}\n\n明天最高气温：{}℃\n\n明天最低气温：{}\
    ℃\n\n明天白天天气：{}\n\n明天夜间天气：{}'.format(data, tempMax, tempMin, textDay, textNight, data1, tempMax1,
                                                    tempMin1, textDay1, textNight1)

content = {
    "title": title,
    "desp": desp
}


def send_email(desp, from_mail, to_mial, right_code):
    HOST = 'smtp.qq.com'
    # 设置邮件标题
    SUBJECT = '今日份天气预报信息!请查收'
    # 设置发件人邮箱
    FROM = from_mail
    # 设置收件人邮箱
    TO = to_mial
    message = MIMEMultipart('related')

    # --------------------------------------发送文本-----------------
    # 发送邮件正文到对方的邮箱中
    message_html = MIMEText(desp, 'plain', 'utf-8')
    message.attach(message_html)

    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮件标题
    message['Subject'] = SUBJECT

    # 获取简单邮件传输协议的证书
    email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
    # 设置发件人邮箱的域名和端口，端口为465
    email_client.connect(HOST, '465')

    # ---------------------------邮箱授权码------------------------------
    result = email_client.login(FROM, right_code)
    print('登录结果', result)
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    # 关闭邮件发送客户端
    email_client.close()
if SCKEY == '':
    send_email(desp, from_mail, to_mial, right_code)
else:
    # server酱Send key
    url = 'https://sctapi.ftqq.com/{}.send'.format(SCKEY)
    requests.post(url=url, data=content)
