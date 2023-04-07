import requests, json, re
# 这里填写COOKIE
cookie = ''
# 这里是SERVER酱的推送方式，不想用的话直接忽略
SCKEY = ''
# 推送plus token
Token = ''
#推送函数
def push(content):
    if SCKEY != '':
        url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, 'MT论坛签到', content)
        requests.post(url)
        print('推送完成')
    elif Token != '':
        headers = {'Content-Type': 'application/json'}
        json = {"token": Token, 'title': 'MT论坛签到', 'content': content, "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')
    else:
        print('未使用消息推送推送！')

login_url = 'https://bbs.binmt.cc/k_misign-sign.html?operation=qiandao&format=button&formhash=9bd09079&inajax=1&ajaxtarget=midaben_sign'
header = {

    'referer': 'https://bbs.binmt.cc/index.php',
    'cookie' : cookie,
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
try:
    info_html = requests.get(url=login_url, headers=header).text
    print(info_html)
    content ="".join(re.findall('<root><!(.*?)></root>',info_html, re.S))
    print(content)
    push(content)
except:
    content = '签到失败，可能COOKIE失效'
    print(content)
    push(content)
