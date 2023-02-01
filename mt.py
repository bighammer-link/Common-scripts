import requests, json, re
# 这里填写COOKIE
cookie = ''
# 这里是SERVER酱的推送方式，不想用的话直接忽略
SCKEY = ''

login_url = 'https://bbs.binmt.cc/k_misign-sign.html?operation=qiandao&format=button&formhash=cf50c078&inajax=1&ajaxtarget=midaben_sign'
header = {

    'referer': 'https://bbs.binmt.cc/index.php',
    'cookie' : cookie,
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
try:
    info_html = requests.get(url=login_url,headers=header).text
    content ="".join(re.findall('<root><!(.*?)></root>',info_html, re.S))
    print(content)
    if SCKEY != "":
        requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, "MT论坛签到", content))
except:
    content = '签到失败，可能COOKIE失效'
    print(content)
    if SCKEY != "":
        requests.post("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, "MT论坛签到", content))
