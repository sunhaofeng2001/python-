from data.mat import show
from data.cha import show1
from data.ss import main
from data.ch import show3
from mapa.mappp import show_map
from kouzhao import kou
import os
def ssa():
    s=input("1.获取省份信息 2.获取城市信息 3.获取国内省份图表 4.获取省内城市图表 5.获取全国疫情地图:")
    if(s=="1"):
        main()
    elif(s=="2"):
        show1()
    elif(s=="3"):
        show()
    elif(s=="4"):
        show3()
    elif(s=="5"):
        show_map()
        os.system('mapp.bat')
    else:
        sse()

def ssb():
    kou()

def sse():
    a = input("1.获取疫情数据,2.判断是否戴口罩口罩输入,3.退出程序:")
    if a == "1":
        ssa()
        return 1
    elif a == "2":
        ssb()
        return 1
    elif a=="3":
        return 0
    else:
        print("输入错误")
        return 1
n=1
while n:
    n=sse()
