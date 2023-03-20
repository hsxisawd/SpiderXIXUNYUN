import requests
import json
from fake_useragent import UserAgent
from setting import Config
import base64
from Crypto.Cipher import PKCS1_v1_5 as PKCS15
from Crypto.PublicKey import RSA
class SignIn(object):

    def __init__(self):
        self.userdata = Config.UserInfo
        self.SignIninfo=Config.SignIninfo
        self.UA = UserAgent()

    def SignIn(self,token):
        url='https://api.xixunyun.com/signin_rsa'
        headers = {"user-agent": self.UA.random}
        params={
            'token': token,
            'entrance_year': 0,
            'graduate_year': 0,
            'school_id': self.userdata['schoolNum']
        }
        data=Config.SignIninfo
        data['longitude'],data['latitude'] = self.Location_encrpt({
            'lng':self.SignIninfo['longitude'],
            'lat': self.SignIninfo['latitude']
        })

        response=requests.post(url,headers=headers,data=data,params=params)
        if response.status_code == 200:
            LoginInfo=response.text
            return json.loads(LoginInfo)

    def Location_encrpt(self,dictData):
        #'lng': 114.23277768904661, 'lat': 22.642906748311876

        key ="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlYsiV3DsG+t8OFMLyhdmG2P2J4GJwmwb1rKKcDZmTxEphPiYTeFIg4IFEiqDCATAPHs8UHypphZTK6LlzANyTzl9LjQS6BYVQk81LhQ29dxyrXgwkRw9RdWaMPtcXRD4h6ovx6FQjwQlBM5vaHaJOHhEorHOSyd/deTvcS+hRSQIDAQAB"
        PUBkey="-----BEGIN PUBLIC KEY-----\n"+key+"\n-----END PUBLIC KEY-----"
        rsakey=RSA.importKey(PUBkey)
        cipher=PKCS15.new(rsakey)
        cipher_Lng=base64.b64encode(cipher.encrypt(dictData['lng'].encode()))
        cipher_Lat = base64.b64encode(cipher.encrypt(dictData['lat'].encode()))

        return cipher_Lng,cipher_Lat