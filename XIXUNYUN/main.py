from StartApp.Login import Login
from StartApp.SignIn import SignIn
from setting import Config
from schedule import every, run_pending
import time
from Unit.log import log
from Unit import AutoMessageWX
import sys
import os


def job():
    token = Login().login()['data']['token']
    messdata = SignIn().SignIn(token)
    if messdata['code']==64033:
        messdata['data']['message_string']="不好意思，今天已经打过卡啦！！"
    AutoMessageData={
                    "Username":{
                        'value':Config.UserInfo['username'],
                    },
                    "SignTime":{
                        'value': time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                    },
                    'Address':{
                        'value':Config.SignIninfo['address']
                    },
                    'Message':{
                        'value':messdata['data']['message_string']
                    }
                }

    Automessdata = AutoMessageWX.AutoMessageToWX().run(AutoMessageData)
    log(messdata,Automessdata)

if __name__ == "__main__":
    sys.path.append(os.getcwd())
    job()
