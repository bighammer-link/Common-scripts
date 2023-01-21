import json

import requests
import re
import time
#填写cookie，（登录到汽车之家，点击个人头像转到我的汽车之家界面，抓取该页面的cookie）
cookie = ''
#推送方式使用的是server酱，填写server酱的SCKEY
SCKEY = ''

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
requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY,"汽车之家签到",content))
