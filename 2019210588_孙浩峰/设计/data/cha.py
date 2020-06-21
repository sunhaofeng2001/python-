import time, json, requests

def show1():
    # 抓取腾讯疫情实时json数据
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'
    data = json.loads(requests.get(url=url).json()['data'])
    # 统计省份信息(34个省份 湖北 广东 河南 浙江 湖南 安徽....)
    num = data['areaTree'][0]['children']
    a = input("输入你所要查询的城市所在省份:")
    k = 0
    for item in num:
        # print(item['name'],end=" ")   # 不换行
        if item['name'] in a:
            # print("")
            # print(item['name'], k)
            break
        k = k + 1

    gz = num[k]['children']

    # ------------------------------------------------------------------------------
    # 第二步：解析数据
    # ------------------------------------------------------------------------------
    # 解析确诊数据
    total_data = {}
    for item in gz:
        if item['name'] not in total_data:
            total_data.update({item['name']: 0})
        total_data[item['name']] = item['total']['confirm']
    names = total_data.keys()
    nums = total_data.values()
    ss = input("请输入城市名称:")
    n1 = 0
    for (a, b) in zip(names, nums):
        if a == ss:
            print("当前日期是:", end=" “")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), end="” ")
            print("地点:", end=" “")
            print(a, end="” 总确诊人数:“")
            print(b, end="” 疑似确诊人数:“")
            n1 = int(b)

    # 解析疑似数据
    total_suspect_data = {}
    for item in gz:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: 0})
        total_suspect_data[item['name']] = item['total']['suspect']
    names = total_suspect_data.keys()
    nums = total_suspect_data.values()
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b, end="” 死亡人数:“")

    # 解析死亡数据
    total_dead_data = {}
    for item in gz:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: 0})
        total_dead_data[item['name']] = item['total']['dead']
    names = total_dead_data.keys()
    nums = total_dead_data.values()
    n2 = 0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b, end="” 治愈人数:“")
            n2 = int(b)

    # 解析治愈数据
    total_heal_data = {}
    for item in gz:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: 0})
        total_heal_data[item['name']] = item['total']['heal']
    names = total_heal_data.keys()
    nums = total_heal_data.values()
    n3 = 0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b, end="” 新增确诊人数:“")
            n3 = int(b)

    # 解析新增确诊数据
    total_new_data = {}
    for item in gz:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: 0})
        total_new_data[item['name']] = item['today']['confirm']  # today
    names = total_new_data.keys()
    nums = total_new_data.values()
    n4 = 0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b, end="” 现存确诊人数:“")
            n4 = int(b)
    print(n1 - n2 - n3 - n4, end="”")
    print("")
