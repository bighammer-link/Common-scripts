import json
import  requests

# refresh_token是一成不变的呢，我们使用它来更新签到需要的access_token，
# refresh_token获取教程：https://github.com/bighammer-link/Common-scripts/wiki/%E9%98%BF%E9%87%8C%E4%BA%91%E7%9B%98refresh_token%E8%8E%B7%E5%8F%96%E6%96%B9%E6%B3%95
refresh_token = ''
# 使用Server酱的推送方式,不想使用的话直接忽略
SCKEY = ''
# 推送加token,使用推送plus，请将token填入下方引号中，不使用的话直接忽略
Token = ''

# 推送函数
def push(content):
    if SCKEY != '':
        url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, '阿里云盘签到', content)
        requests.post(url)
        print('推送完成')
    elif Token != '':
        headers = {'Content-Type': 'application/json'}
        json = {"token": Token, 'title': '阿里云盘签到', 'content': content, "template": "json"}
        resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')
    else:
        print('未使用消息推送推送！')
# 签到函数
def daily_check(access_token):
    # 进行签到
    url = 'https://member.aliyundrive.com/v1/activity/sign_in_list?_rx-s=mobile'
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url, headers=headers, json={}).text
    result = json.loads(response)
    # print(result)
    # 进行奖励领取
    url_reward = 'https://member.aliyundrive.com/v1/activity/sign_in_reward?_rx-s=mobile'
    resp2 = requests.post(url=url_reward, headers=headers, data=json.dumps({'signInDay':result['result']['signInCount']}))
    result2 = json.loads(resp2.text)
    # print(result2)
    if 'success' in result:
        print('签到成功')
        for i, j in enumerate(result['result']['signInLogs']):
            if j['status'] == 'miss':
                day_json = result['result']['signInLogs'][i-1]
                # print(day_json)
                # print(day_json['isReward'])
                if not day_json['isReward']:
                    content = '签到成功，今日未获得奖励'
                else:
                    content = '本月累计签到{}天,今日签到获得{}{}'.format(result['result']['signInCount'],
                                                                         day_json['reward']['name'],
                                                                         day_json['reward']['description'])
                print(content)
                return content


# 使用refresh_token更新access_token
def update_token(refresh_token):
    url = 'https://auth.aliyundrive.com/v2/account/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(url=url, json=data).json()
    access_token = response['access_token']
    print('获取的access_token为{}'.format(access_token))
    return access_token


def mian():
    print('更新access_token')
    access_token = update_token(refresh_token)
    print('更新成功，开始进行签到')
    content = daily_check(access_token)
    push(content)


if __name__ == '__main__':
    mian()
