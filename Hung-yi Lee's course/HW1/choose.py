# -*-coding:utf-8 -*-
# __author__=coco
#通过画图筛选出有用的数据，避免冗余计算
import matplotlib.pyplot as plt
import csv
import random
import math
data =[]#数据

reader=csv.reader(open('train.csv', encoding='gbk',errors="ignore"))
for item in reader:
    data.append(item)
    #print(item)
data=data[1:len(data)]
for i in range(len(data)):#对数据进行一些处理，分割出有效数值部分
    data[i]=data[i][3:27]
    if i%18==10:
        for j in range(24):
            data[i][j]=0
    else:
        for j in range(24):
            data[i][j]=float(data[i][j])
    #print(data[i])

x=range(24)
plt.plot(x,data[27],color='r')
plt.plot(x,data[35])
plt.plot(x,data[52])
plt.plot(x,data[70])
plt.show()