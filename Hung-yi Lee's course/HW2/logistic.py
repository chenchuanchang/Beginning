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
        x[IDnum_x].append(int(j))
    # print (x[IDnum_x])
    IDnum_x=IDnum_x+1

# print(IDnum_x)
for i in x[0]:
    w.append(random.uniform(0,0.1))
    wx.append(0)
    Wnum_x=Wnum_x+1
w[0]=random.uniform(0.00001,0.001)
w[1]=-random.uniform(0.00001,0.0001)
w[3]=random.uniform(0.00001,0.0001)
w[5]=random.uniform(0.00001,0.001)
f = open("Y_train")
flag = False
for i in f:
    if flag==False:
        flag=True
        continue
    y.append(int(i[0:1]))
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
        if error>lasterror:
            return b
        else:
            lasterror=error
        print("第"+str(t+1)+"次迭代   误差为："+str(error)+"   正确率为："+str((IDnum_x-error)/IDnum_x))
        print(w)
    return b
b=DG(0.0000000000000001,1000,0)

f = open("para.txt",'w')
for i in range(len(w)):
    f.write(str(w[i])+'\n')
f.write(str(b))
f.close()