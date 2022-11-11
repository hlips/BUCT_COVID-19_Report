import json
import time

import requests

url = "https://eai.buct.edu.cn/ncov/wap/default/save"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046125 Mobile Safari/537.36 wxwork/4.0.16 MicroMessenger/7.0.1'
}

name = '李显龙'
cookies = {
    'eai-sess':'buctreport666666homo114514', # 企业微信页面cookie
}
data = {
    'sfzx': '0',  # 是否在校
    'sfzgn': '1',   # 所在地点中国大陆
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

    'area': '西藏自治区 日喀则市 定日县',  # 所在区域
    'province': '西藏自治区',  # 所在省
    'city': '日喀则市',  # 所在市
    'address': '西藏自治区日喀则市定日县珠峰4000米核酸检测点',  # 道路地址
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
        'accuracy': None,
        'isConverted': True,
        'addressComponent': {
            'citycode': '0892',  # 区号
            'adcode': '540200',  # 行政区划代码
            'businessAreas': [],
            'neighborhoodType': '',
            'neighborhood': '',
            'building': '',
            'buildingType': '',
            'street': '珠峰路',     # 所在道路
            'streetNumber': '1号',  # 
            'country': '中国',      # 所在地区
            'province': '西藏自治区',  # 所在省
            'city': '日喀则市',  # 所在市
            'district': '定日县',  # 所在区
            'township': ''  # 所在街道
        },
        'formattedAddress': '西藏自治区日喀则市定日县珠峰4000米核酸检测点',  # 拼接后的地址
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
            + name + ' ' + data['city'] + ' ' + json.loads(result.text)['m'])
        break
    except requests.exceptions.ConnectionError:
        print(time.strftime("%m/%d %H:%M:%S ", time.localtime())+ name + ' 网络异常！')
        connect_times += 1
        time.sleep(9)
        continue
