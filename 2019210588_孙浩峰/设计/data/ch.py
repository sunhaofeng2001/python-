import  json, requests
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def show3():
    try:
        # 抓取腾讯疫情实时json数据
        url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'
        data = json.loads(requests.get(url=url).json()['data'])
        # 统计省份信息
        num = data['areaTree'][0]['children']
        a = input("输入你所要查询的省份:")
        k = 0
        for item in num:
            if item['name'] in a:
                break
            k = k + 1

        gz = num[k]['children']

        # 第二步：解析数据
        # 解析确诊数据
        total_data = {}
        for item in gz:
            if item['name'] not in total_data:
                total_data.update({item['name']: 0})
            total_data[item['name']] = item['total']['confirm']

        # 解析疑似数据
        total_suspect_data = {}
        for item in gz:
            if item['name'] not in total_suspect_data:
                total_suspect_data.update({item['name']: 0})
            total_suspect_data[item['name']] = item['total']['suspect']

        # 解析死亡数据
        total_dead_data = {}
        for item in gz:
            if item['name'] not in total_dead_data:
                total_dead_data.update({item['name']: 0})
            total_dead_data[item['name']] = item['total']['dead']

        # 解析治愈数据
        total_heal_data = {}
        for item in gz:
            if item['name'] not in total_heal_data:
                total_heal_data.update({item['name']: 0})
            total_heal_data[item['name']] = item['total']['heal']

        # 解析新增确诊数据
        total_new_data = {}
        for item in gz:
            if item['name'] not in total_new_data:
                total_new_data.update({item['name']: 0})
            total_new_data[item['name']] = item['today']['confirm']  # today

        names = list(total_data.keys())  # 省份名称
        num1 = list(total_data.values())  # 确诊数据
        num2 = list(total_suspect_data.values())
        num3 = list(total_dead_data.values())  # 死亡数据
        num4 = list(total_heal_data.values())  # 治愈数据
        num5 = list(total_new_data.values())  # 新增确诊病例
        n = time.strftime("%Y-%m-%d") + "-{}-4db.csv".format(a)
        fw = open(n, 'w', encoding='utf-8')
        fw.write('province,type,data\n')
        i = 0
        while i < len(names):
            fw.write(names[i] + ',confirm,' + str(num1[i]) + '\n')
            fw.write(names[i] + ',dead,' + str(num3[i]) + '\n')
            fw.write(names[i] + ',heal,' + str(num4[i]) + '\n')
            fw.write(names[i] + ',new_confirm,' + str(num5[i]) + '\n')
            i = i + 1
        else:
            fw.close()

        # ------------------------------------------------------------------------------
        # 调用Seaborn绘制柱状图
        # 读取数据
        n = time.strftime("%Y-%m-%d") + "-{}-4db.csv".format(a)
        data = pd.read_csv(n)

        # 设置窗口
        fig, ax = plt.subplots(1, 1)
        # 设置绘图风格及字体
        sns.set_style("whitegrid", {'font.sans-serif': ['simhei', 'Arial']})

        # 绘制柱状图
        g = sns.barplot(x="province", y="data", hue="type", data=data, ax=ax,
                        palette=sns.color_palette("hls", 8))

        # 设置Axes的标题
        ax.set_title('{}疫情最新情况'.format(a))

        # 设置坐标轴文字方向
        ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)

        # 设置坐标轴刻度的字体大小
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=8)

        plt.show()
    except:
        print("输入错误")


