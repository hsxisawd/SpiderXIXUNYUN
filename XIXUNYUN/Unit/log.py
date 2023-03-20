import time



def log(SignInfo,AutoWxInfo):
    timeNow=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    title=f"----------------------------{timeNow}---------------------------\n"
    floor="\n-------------------------------------------------------------------\n"

    with open('LogFile/log.txt','a',encoding='utf-8') as f:
        f.write(
            title+
            "签到日志"+str(SignInfo)+"\n"+
            "发送日志" +str(AutoWxInfo)+"\n"+
            floor)