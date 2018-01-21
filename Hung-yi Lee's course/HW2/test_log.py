# -*-coding:utf-8 -*-
# __author__=coco

import numpy as np
import pandas as pa
import math

y=pa.read_csv("correct_answer.csv",sep=',',header=0)
y=np.array(y.values)
w=[]
f=open("para.txt")
for i in f:
    w.append(float(i[0:len(i)-1]))
Wnum_x=len(w)
x=[]
IDnum_x=0
f = open("X_test")
# print(f)
flag=False
for i in f:
    # print(i)
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

nomal(x)
# print (x[0])
def func(i,b):
    res=b
    for k in range(Wnum_x-1):
        res=res+x[i][k]*w[k]
    # print (res)
    if (-res)>1000:
        ans=1
    else:
        E=math.exp(-res)
        # print (E)
        ans = 1/(1+E)
    if ans>0.5:
        return 1
    else:
        return 0
error=0
for i in range(IDnum_x):
    fx=func(i,w[Wnum_x-1])
    if(fx==y[i][1]):
        error=error+1
print("错误个数："+str(IDnum_x-error))
print("正确率为："+str(error/IDnum_x))

# print(y)