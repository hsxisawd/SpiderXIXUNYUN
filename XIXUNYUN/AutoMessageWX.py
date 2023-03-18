import json
import time
import setting
import requests
from fake_useragent import UserAgent


class AutoMessageToWX(object):

    def __init__(self):
        self.openid = setting.Config.WxXinInfo['openID']
        self.secret = setting.Config.WxXinInfo["secret"]
        self.template_id=setting.Config.WxXinInfo["templateID"]
        UA = UserAgent()
        self.headers = {"user-agent": UA.random}

    def get_access_token(self):
        access_url = 'https://api.weixin.qq.com/cgi-bin/token'
        params = {
            'grant_type': 'client_credential',
            'appid': self.openid,
            'secret': self.secret
        }
        response = requests.get(access_url, headers=self.headers, params=params).json()
        self.get_openid(response["access_token"])

    def get_openid(self, access_token):
        OpenIDurl = f"https://api.weixin.qq.com/cgi-bin/user/get"
        params = {
            'access_token': access_token,
            'next_openid': ''
        }
        response = requests.get(OpenIDurl, headers=self.headers, params=params).json()
        if  response.get('data') != None:
            self.send_message(response['data']['openid'],access_token)

    def send_message(self,data,access_token):
        url ="https://api.weixin.qq.com/cgi-bin/message/template/send"
        params = {"access_token":access_token}
        for openid in data:
            message_json = {
                "touser": openid,
                "template_id": "",
                "url": "http://weixin.qq.com/download",
                "topcolor": "#FF0000",
                "data": {
                    "Username":{
                        'value':'hsxisawd',
                    },
                    "SignTime":{
                        'value': time.time(),
                    },
                    'Address':{
                        'value':'广东省深圳市龙岗区圆山街道'
                    },
                    'Message':{
                        'value':"太棒了！+2积分，您已签到2天。"
                    }

                }
            }
            message_data=bytes(json.dumps(message_json,ensure_ascii=False).encode('utf-8'))
            response=requests.post(url,headers=self.headers,params=params,data=message_data)
            result=response.json()
            print(result)

    def run(self):
        self.get_access_token()

