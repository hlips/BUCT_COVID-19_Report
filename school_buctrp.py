import json
import time
import requests

url = "https://eai.buct.edu.cn/ncov/wap/default/save"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046125 Mobile Safari/537.36 wxwork/4.0.16 MicroMessenger/7.0.1'
}

name = '芭芭拉·冯·采列'
cookies = {
    'eai-sess':'buctreport666666homo114514', # 填入企业微信页面cookie
}
data = {
    'ismoved': '0', # 是否位移
    'sfzx': '1',  # 是否在校

    'zgfxdq': '0',  # 中高风险地区
    "buctzctw": "2",    # 今日早晨体温范围(36℃-36.9℃)
    "buctzwtw": "2",    # 今日中午体温范围(36℃-36.9℃)
    "buctwjtw": "2",    # 今日晚间体温范围(36℃-36.9℃)
    'sfcxtz': '0',  # 没有出现发热、乏力、干咳、呼吸困难等症状
    'sfjcbh': '0',  # 今日是否接触无症状感染/疑似/确诊人群
    'mjry': '0',  # 今日是否接触密接人员
    'csmjry': '0',  # 近14日内本人/共同居住者是否去过疫情发生场所
    'sfcyglq': '0',  # 是否处于观察期
    'szsqsfybl': '0',  # 所在社区是否有确诊病例
    'sfcxzysx': '0',  # 是否有任何与疫情相关的， 值得注意的情况
    'jcjgqr': '0',  # 正常，非疑似/确诊

    'area': '北京市 昌平区',  # 所在区域
    'province': '北京市',  # 所在省
    'city': '北京市',  # 所在市
    'address': '北京市昌平区南口镇南涧路29号北京化工大学昌平校区',  # 地址
    'qksm': '',  #其他情况

    'geo_api_info': {
        'type': 'complete', 'info': 'SUCCESS', 'status': 1,
        'position': {
            'R': 113.0270592,  # 经度
            'Q': 22.5524345,  # 纬度
            'lng': 113.0270592,  # 经度
            'lat': 22.5524345  # 纬度
        },
        'message': 'Get geolocation success.Convert Success.Get address success.',
        'location_type': 'geo',
        'accuracy': 40,
        'isConverted': True,
        'addressComponent': {
            'citycode': '010',
            'adcode': '110114',  # 行政区划代码
            'businessAreas': [],
            'neighborhoodType': '',
            'neighborhood': '',
            'building': '',
            'buildingType': '',
            'street': '南涧路',
            'streetNumber': '29号',
            'country': '中国',
            'province': '北京市',  # 所在省
            'city': '北京市',  # 所在市
            'district': '昌平区',  # 所在区
            'township': ''  # 所在街道
        },
        'formattedAddress': '北京市昌平区南口镇南涧路29号北京化工大学昌平校区',  # 拼接后的地址
        'roads': [],
        'crosses': [],
        'pois': []
    },
}

connect_times = 0
while connect_times < 3:
    buct_session = requests.Session()
    try:
        result = buct_session.post(url, data=data, headers=headers, cookies=cookies, timeout=15)
        print(
            "北化疫情打卡 " + time.strftime("%m月%d日 %H:%M:%S ", time.localtime())
            + name + ' ' + json.loads(result.text)['m'])
        break
    except requests.exceptions.ConnectionError:
        print(time.strftime("%m/%d %H:%M:%S ", time.localtime())+ name + ' 网络异常！')
        connect_times += 1
        time.sleep(9)
        continue
