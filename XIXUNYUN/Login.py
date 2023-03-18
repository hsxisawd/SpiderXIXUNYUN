import requests
import json
import base64
from fake_useragent import UserAgent
import setting

class Login(object):

    def __init__(self):

        self.userdata =setting.Config.UserInfo
        self.UA=UserAgent()

    def login(self):

        headers={"user-agent":self.UA.random}
        url="https://api.xixunyun.com/login/admin"
        j_data=self.UserBase64()
        data={
            'j_data': j_data,
            'type': 'web',
            'school_id': self.userdata["schoolNum"],
            'alg': 'en001'
        }
        response=requests.post(url,headers=headers,data=data)
        if response.status_code == 200:
            LoginInfo=response.text

            return json.loads(LoginInfo)

    def UserBase64(self):
        username=self.userdata['username']
        password=self.userdata['password']
        #ZDIwYzA1MDE0O2MwNTAxNDsx
        return  base64.b64encode(f'{username};{password};1'.encode('utf-8')).decode('utf-8')

