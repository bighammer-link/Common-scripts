import json

import requests
import re
import time
#填写cookie，（登录到汽车之家，点击个人头像转到我的汽车之家界面，抓取该页面的cookie。）
cookie = ''
#推送方式使用的是server酱，填写server酱的SCKEY
SCKEY = ''
# 推送PLUS的token
Token = ''
# 推送函数
def push(content):
    if SCKEY != '':
        url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, '汽车之家签到', content)
        requests.post(url)
        print('推送完成')
    elif Token != '':
        headers = {'Content-Type': 'application/json'}
        json = {"token": Token, 'title': '汽车之家签到', 'content': content, "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')
    else:
        print('未使用消息推送推送！')

url = 'https://i.autohome.com.cn/'
check_url='https://i.autohome.com.cn/ajax/usersign/UserSign'


header={
    'cookie':cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

}
# # 获取账号名称
html_info = requests.post(url,headers=header).text
info = "".join(re.findall('<h1 class="user-name"><b>(.*?)</b>', html_info, re.S))
# # 进行签到
html = requests.get(url=check_url,headers=header).text
result = json.loads(html)['msg']
count = json.loads(html)['signCount']
content = '{}{}已累计签到{}天'.format(info,result,count)
# requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY,"汽车之家签到",content))

print(content)
push(content)
