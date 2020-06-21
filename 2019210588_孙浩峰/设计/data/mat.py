import time, json, requests

def show():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'
    data = json.loads(requests.get(url=url).json()['data'])

    # 统计省份信息
    num = data['areaTree'][0]['children']
    # 解析确诊数据
    total_data = {}
    for item in num:
        if item['name'] not in total_data:
            total_data.update({item['name']: 0})
        for city_data in item['children']:
            total_data[item['name']] += int(city_data['total']['confirm'])

    # 解析疑似数据
    total_suspect_data = {}
    for item in num:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: 0})
        for city_data in item['children']:
            total_suspect_data[item['name']] += int(city_data['total']['suspect'])

    # 解析死亡数据
    total_dead_data = {}
    for item in num:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: 0})
        for city_data in item['children']:
            total_dead_data[item['name']] += int(city_data['total']['dead'])

    # 解析治愈数据
    total_heal_data = {}
    for item in num:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: 0})
        for city_data in item['children']:
            total_heal_data[item['name']] += int(city_data['total']['heal'])

    # 解析新增确诊数据
    total_new_data = {}
    for item in num:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: 0})
        for city_data in item['children']:
            total_new_data[item['name']] += int(city_data['today']['confirm'])  # today

    # ------------------------------------------------------------------------------
    # 第二步：绘制柱状图
    # ------------------------------------------------------------------------------
    import matplotlib.pyplot as plt

    plt.figure(figsize=[10, 6])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # -----------------------------1.绘制确诊数据-----------------------------------
    p1 = plt.subplot(221)

    # 获取数据
    names = total_data.keys()
    nums = total_data.values()
    plt.bar(names, nums, width=0.3, color='green')

    # 设置标题
    plt.ylabel("确诊人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    # 显示数字
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p1)

    # -----------------------------2.绘制新增确诊数据-----------------------------------
    p2 = plt.subplot(222)
    names = total_new_data.keys()
    nums = total_new_data.values()
    plt.bar(names, nums, width=0.3, color='yellow')
    plt.ylabel("新增确诊人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    # 显示数字
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p2)

    # -----------------------------3.绘制死亡数据-----------------------------------
    p3 = plt.subplot(223)
    names = total_dead_data.keys()
    nums = total_dead_data.values()
    plt.bar(names, nums, width=0.3, color='blue')
    plt.xlabel("地区")
    plt.ylabel("死亡人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p3)

    # -----------------------------4.绘制治愈数据-----------------------------------
    p4 = plt.subplot(224)
    names = total_heal_data.keys()
    nums = total_heal_data.values()
    plt.bar(names, nums, width=0.3, color='red')
    plt.xlabel("地区")
    plt.ylabel("治愈人数", rotation=90)
    plt.xticks(list(names), rotation=-60, size=8)
    for a, b in zip(list(names), list(nums)):
        plt.text(a, b, b, ha='center', va='bottom', size=6)
    plt.sca(p4)
    plt.show()
