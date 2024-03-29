import requests, json,re,time
# 这里是登录到某个主播鱼吧后抓取的cookie
cookie = ''
# 这里是某主播鱼吧的id号，就是登录某主播鱼吧后，地址栏中的最后几位数字
group_id =
# 这里是server酱的推送key。不想使用的话，直接忽略
SCKEY = ''
# 推送plus的token。不想使用的话直接忽略。
Token = ''
# 推送函数
def push(content):
    if SCKEY != '':
        url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, '斗鱼鱼吧签到', content)
        requests.post(url)
        print('推送完成')
    elif Token != '':
        headers = {'Content-Type': 'application/json'}
        json = {"token": Token, 'title': '斗鱼鱼吧签到', 'content': content, "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')
    else:
        print('未使用消息推送推送！')
url_check = 'https://yuba.douyu.com/ybapi/topic/sign?timestamp='+str(int(time.time() / 100))
headers = {
    "authority": "yuba.douyu.com",
    "method": "POST",
    "path": "/ybapi/topic/sign?timestamp=" + str(int(time.time() / 100)),
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-length": "23",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": cookie,
    "origin": "https://yuba.douyu.com",
    "referer": "https://yuba.douyu.com/group/"+str(group_id),
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform":"Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "x-csrf-token": "hbxPpC1SYvWyptPnO054gAXkiKtODAZg"
}
data = {
'group_id': group_id
}
html = requests.post(url=url_check, headers=headers,data=data)
result = json.loads(html.text)['status_code']

if result == 200:
    content ='签到成功'
    print(content)
    push(content)
elif result == 1001:
    content = '今天已经签到了'
    print(content)
    push(content)
else:
    content = '签到失败（可能是cookie失效，请及时更新）'
    print(content)
    push(content)
