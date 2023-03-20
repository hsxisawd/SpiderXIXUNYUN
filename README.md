# 习讯云自动签到打卡（）
## 目录结构

```python
-XIXUNYUN
    │  main.py 				#程序入口文件
    │  requirements.txt		#项目第三方依赖
    │  setting.py			#项目配置文件
    ├─LogFile				#日志存储文件
    ├─StartApp				#打卡程序包
    │  │  Login.py				#登录功能
    │  │  SignIn.py				#签到功能
    ├─test					#测试文件夹
    │      test.py
    ├─Unit					#工具包
    │  │  AutoMessageWX.py		#向微信公众号，发送提醒消息
    │  │  GetBaiDU_Address.py	#通过百度地图获取地址坐标
    │  │  log.py				#生成日志
```

## 程序运行