# -*-coding:utf-8 -*-
# __author__=coco
#预测样本年收入是否大于50W

import math
import random
x=[]
y=[]
w=[]
wx=[]
IDnum_x=0
Wnum_x=0
f = open("X_train")
flag=False
for i in f:
    if flag==False:
        flag=True
        continue
    tem=i[0:len(i)-1].split(",")
    # if IDnum_x<20:
    #     print(tem)
    x.append([])
    for j in tem:
        x[IDnum_x].append(float(j))
    # print (x[IDnum_x])
    IDnum_x=IDnum_x+1

# print(IDnum_x)
for i in x[0]:
    w.append(0)
    wx.append(0)
    Wnum_x=Wnum_x+1

def nomal(x=[]):
    for i in range(6):
        max_x=x[0][i]
        min_x=x[0][i]
        for j in range(len(x)):
            if x[j][i]>max_x:
                max_x=x[j][i]
            if x[j][i]<min_x:
                min_x=x[j][i]
        ran=max_x-min_x
        for j in range(len(x)):
            x[j][i]=(x[j][i]-min_x)/ran

f = open("Y_train")
flag = False
for i in f:
    if flag==False:
        flag=True
        continue
    y.append(float(i[0:1]))
# print (y)

def func(i,b):
    res=b
    for k in range(Wnum_x):
        res=res+x[i][k]*w[k]
    # print (res)
    if (-res)>100:
        ans=1
    else:
        E=math.exp(-res)
        # print (E)
        ans = 1/(1+E)
    if ans>0.5:
        return 1
    else:
        return 0
nomal(x)
# print(x[0])

def Write(b,error,acc):
    f = open("para.txt",'w')
    for i in range(len(w)):
        f.write(str(w[i])+'\n')
    f.write(str(b))
    f.close()
    f=open("para_log.txt",'w')
    f.write(str(error)+'\n')
    f.write(str(acc)+'\n')

def DG(miu,iter,b):
    lasterror=1000000

    for t in range(iter):
        error=0
        bx=0
        for i in range(Wnum_x):
            wx[i]=0
        for i in range(IDnum_x):
            fx=func(i,b)
            if fx!=y[i]:
                error=error+1
            for j in range(Wnum_x):
                wx[j]=wx[j]+(y[i]-fx)*x[i][j]
            bx=bx+y[i]-fx
        for i in range(Wnum_x):
            w[i]=w[i]+miu*wx[i]
            # print(miu*wx[i])
        b=b+miu*bx
        if error<lasterror:
            lasterror=error
            Write(b,error,(IDnum_x-error)/IDnum_x)
        print("第"+str(t+1)+"次迭代   误差为："+str(error)+"   正确率为："+str((IDnum_x-error)/IDnum_x))
        # print(w)
    return b
b=DG(0.000001,100,0)

