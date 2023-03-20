import json
from setting import Config
import requests
from fake_useragent import UserAgent


class AutoMessageToWX(object):

    def __init__(self):
        self.openid = Config.WxXinInfo['openID']
        self.secret = Config.WxXinInfo["secret"]
        self.template_id = Config.WxXinInfo["templateID"]
        UA = UserAgent()
        self.headers = {"user-agent": UA.random}
        self.MessageData = ""

    def get_access_token(self):
        access_url = 'https://api.weixin.qq.com/cgi-bin/token'
        params = {
            'grant_type': 'client_credential',
            'appid': self.openid,
            'secret': self.secret
        }
        response = requests.get(access_url, headers=self.headers, params=params).json()
        return response

    def get_openid(self, access_token):
        OpenIDurl = f"https://api.weixin.qq.com/cgi-bin/user/get"
        params = {
            'access_token': access_token,
            'next_openid': ''
        }

        return requests.get(OpenIDurl, headers=self.headers, params=params).json()

    def send_message(self, data, access_token):
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send"
        params = {"access_token": access_token}
        for openid in data:
            message_json = {
                "touser": openid,
                "template_id": self.template_id,
                "url": "http://weixin.qq.com/download",
                "topcolor": "#FF0000",
                "data": self.MessageData
            }
            message_data = bytes(json.dumps(message_json, ensure_ascii=False).encode('utf-8'))
            response = requests.post(url, headers=self.headers, params=params, data=message_data)
            return response.json()

    def run(self, MessageData):
        self.MessageData = MessageData
        responseA = self.get_access_token()
        print(responseA)
        responseB = self.get_openid(responseA["access_token"])
        if responseB.get('data') != None:
            return self.send_message(responseB['data']['openid'], responseA["access_token"])
