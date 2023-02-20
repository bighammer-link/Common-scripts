import json
import  requests

# refresh_token是一成不变的呢，我们使用它来更新签到需要的access_token
refresh_token = ''
# 使用Server酱的推送方式
SCKEY = ''

#推送函数
def push(content):
    url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, '阿里云盘签到', content)
    requests.post(url)
    print('推送完成')
#签到函数
def daily_check(access_token):
    url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
    headers = {
        'Authorization': access_token
    }
    response = requests.post(url=url, headers=headers, json={}).text
    result = json.loads(response)
    # print(result)
    if 'success' in result:
        print('签到成功')
        for i, j in enumerate(result['result']['signInLogs']):
            if j['status'] == 'miss':
                day_json = result['result']['signInLogs'][i-1]
                # print(day_json)
                if not day_json['isReward']:
                    content = '签到成功，今日未获得奖励'
                else:
                    content = '本月累计签到{}天,今日签到获得{}{}'.format(result['result']['signInCount'],
                                                                     day_json['reward']['name'],
                                                                     day_json['reward']['description'])
                print(content)

                return content

    print()
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
    if SCKEY != '':
        push(content)





if __name__ == '__main__':
    mian()
