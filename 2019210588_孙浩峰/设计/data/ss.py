import time, json, requests

def main():

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'
    data = json.loads(requests.get(url=url).json()['data'])
    num = data['areaTree'][0]['children']


    total_data = {}
    for item in num:
        if item['name'] not in total_data:
            total_data.update({item['name']: 0})
        for city_data in item['children']:
            total_data[item['name']] += int(city_data['total']['confirm'])
    names = total_data.keys()
    nums = total_data.values()
    ss=input("请输入你所要查询的省份:")
    n1=0
    for (a,b) in zip(names,nums):
        if a==ss:
            print("当前日期是:",end=" “")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),end="” ")
            print("地点:",end=" ”")
            print(a,end="” 总确诊人数:“")
            print(b,end="” 疑似确诊人数:“")
            n1=int(b)


    total_suspect_data = {}
    for item in num:
        if item['name'] not in total_suspect_data:
            total_suspect_data.update({item['name']: 0})
        for city_data in item['children']:
            total_suspect_data[item['name']] += int(city_data['total']['suspect'])
    names = total_suspect_data.keys()
    nums = total_suspect_data.values()
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b,end="” 死亡人数:“")


    total_dead_data = {}
    for item in num:
        if item['name'] not in total_dead_data:
            total_dead_data.update({item['name']: 0})
        for city_data in item['children']:
            total_dead_data[item['name']] += int(city_data['total']['dead'])
    names = total_dead_data.keys()
    nums = total_dead_data.values()
    n2=0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b,end="” 治愈人数:“")
            n2=int(b)


    total_heal_data = {}
    for item in num:
        if item['name'] not in total_heal_data:
            total_heal_data.update({item['name']: 0})
        for city_data in item['children']:
            total_heal_data[item['name']] += int(city_data['total']['heal'])
    names = total_heal_data.keys()
    nums = total_heal_data.values()
    n3=0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b,end="” 新增确诊人数:“")
            n3=int(b)


    total_new_data = {}
    for item in num:
        if item['name'] not in total_new_data:
            total_new_data.update({item['name']: 0})
        for city_data in item['children']:
            total_new_data[item['name']] += int(city_data['today']['confirm'])
    names = total_new_data.keys()
    nums = total_new_data.values()
    n4=0
    for (a, b) in zip(names, nums):
        if a == ss:
            print(b,end="” 现存确诊人数:“")
            n4=int(b)

    print(n1-n2-n3-n4,end="”")
    print("")
