class Config(object):
    SignIninfo = {
        'change_sign_resource': 0,
        'address': '地址',
        'remark': 0,
        'comment': 0,
        'longitude': '经度',
        'latitude': '纬度',
        'platform': 'h5',
        'address_name': '地址名',
        'file': "",
        'province': '省份',
        'city': '城市',
        'district': '区名',
    }
    UserInfo = {
        'username': "用户名",
        'password': "密码",
        'schoolNum': "学校代码"
    }
    #自动获取经纬度配置
    BaiduApiInfo = {
        'BaiDuAK': "百度地图AK",
        'Api_url': "https://api.map.baidu.com/geocoding/v3/"
    }
    #发送到微信公众号，测试版
    WxXinInfo = {
        'openID': '公众号Appid',
        'secret': '公众号secret',
        'templateID': '模板ID'
    }

