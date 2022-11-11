# BUCT_COVID-19_Report

基于 Python3 的适用于北京化工大学的 COVID-19 自动填报脚本  

项目用于学习交流，仅用于各项无异常时打卡，如有身体不适等情况还请自行如实打卡

## 使用方式

1. 打开企业微信，按`Ctrl+Alt+Shift+D`组合键进入调试模式。进入“返校打卡”页面，右键单击，在DevTools“网络”页面获得`cookies`中`eai-sess`项的值
![获取cookie](images/get_cookie.png)
2. (可选) 修改 `report.py` 内的经纬度，可使用[百度地图开放平台](https://api.map.baidu.com/lbsapi/getpoint/)进行取点

## 自动化
### Linux：使用 Crontab

```shell script
crontab -e
```

（以脚本放置在`~/scripts/`目录为例）

每天晚上18点上报：
```shell script
1 18 * * * python3 report.py
```

每天晚上18点上报并追加输出到日志：
```shell script
1 18 * * * python ~/scripts/home_buctrp.py >> report.log
```

### Windows：任务计划程序
1. 右键单击`Windows徽标键`，选择`计算机管理`；
2. 选择 `系统工具` → `任务计划程序` ，点击右侧的 `创建基本任务`，进入`创建基本任务向导`窗口；
3. 参考这篇CSDN博文：[Windows创建定时任务执行Python脚本](https://blog.csdn.net/u012849872/article/details/82719372)进行设置。
