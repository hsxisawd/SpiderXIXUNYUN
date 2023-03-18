import requests
import json
import setting

class GetAddressApi(object):

    def __init__(self):
        self.Baidu=setting.Config.BaiduApiInfo
    def get_address(self,address):

        params={
            'address':address,
            "ak":self.Baidu['BaiDuAK'],
            "output":'json',
            'extension_analys_level':1
        }
        response = requests.get(self.Baidu['Api_url'],params=params)
        if response.status_code == 200:
            addressInfo=response.text

            return json.loads(addressInfo)
        return "请求失败！"



