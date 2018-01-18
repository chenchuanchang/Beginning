# -*-coding:utf-8 -*-
# __author__=coco
#取前9个小时的所有数据，推测第10个小时的PM2.5
import csv
import random
import math
data =[]#数据
w=[]
wx=[]
lg=[]
global b
b=-26
global lgb
lgb=0
global datelen
datelen=4

reader=csv.reader(open('train.csv', encoding='gbk',errors="ignore"))
for item in reader:
    data.append(item)
    #print(item)
data=data[1:len(data)]
for i in range(len(data)):#对数据进行一些处理，分割出有效数值部分
    data[i]=data[i][3:27]
    if i%18==10:
        for j in range(24):
            data[i][j]=0.00001
    else:
        for j in range(24):
            data[i][j]=float(data[i][j])
    #print(data[i])

for i in range(239,-1,-1):#去除无效数据0-6、10、12-13、16-17,
    # 最终有效为6个
    for j in range(17,15,-1):
        del data[i*18+j]
    for j in range(13,11,-1):
        del data[i*18+j]
    del data[i*18+10]
    for j in range(6,-1,-1):
        del data[i*18+j]
# #归一化处理
# for k in range(10):
#     max=data[k][0]
#     min=data[k][0]
#     for i in range(240):
#         for j in range(24):
#             if data[i*10+k][j] >max:
#                 max=data[i*10+k][j]
#             if data[i*10+k][j] <min:
#                 min=data[i*10+k][j]
#     GAP=max-min
#     for i in range(240):
#         for j in range(24):
#             data[i*10+k][j]=(data[i*10+k][j]-min)/GAP

for i in range(6):#初始化系数
    w.append([])
    wx.append([])
    lg.append([])
    for j in range(datelen):
        wx[i].append(0)
        lg[i].append(0)
        w[i].append(0.1)


for d in range(240):
    for i in range(6):
        left=0
        for j in range(23-datelen):
            left=left+data[d*6+i][j]
        for j in range(23-datelen,23):
            wx[i][j+datelen-23]=wx[i][j+datelen-23]+left
            left=left+data[d*6+i][j]-data[d*6+i][j+datelen-23]
for i in range(6):
    for j in range(datelen):
        wx[i][j]=wx[i][j]/(240*(24-datelen))
# print(wx)
def func(i,j):
    res=b
    global datelen
    for k in range(6):
        for q in range(datelen):
            res=res+w[k][q]*data[k+i*6][j+q]
    return res

def DG(miu,iter):
    global datelen
    for t in range(iter):
        error = 0
        g = 0
        for i in range(240):
            for j in range(24-datelen):
                tem=func(i,j)-data[2+i*6][j+datelen]
                g=g+tem
                error=error+tem**2
        for i in range(6):
            for j in range(datelen):
                G=g*2*wx[i][j]
                # print(G)
                lg[i][j]=lg[i][j]+G**2
                #print (wx[i][j])
                w[i][j]=w[i][j]-(miu*G)
                # print(miu*G)
        G=g*2
        global lgb
        lgb=lgb+G**2
        global b
        b=b-(miu*G)
        print("第"+str(t+1)+"次迭代   误差为："+str(error/(240*(24-datelen))))
DG(0.0000000001,200)


f = open("para.txt",'w')
for i in range(6):
    for j in w[i]:
        f.write(str(j)+' ')
    f.write("\n")
f.write(str(b))
f.close()