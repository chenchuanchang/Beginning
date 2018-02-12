# -*-coding:utf-8 -*-
# __author__=coco
#对数据进行测试
import csv

data=[]
w=[]
global datelen
datelen=4
reader=csv.reader(open('test.csv', encoding='gbk',errors="ignore"))
for item in reader:
    data.append(item)
for i in range(len(data)):#对数据进行一些处理，分割出有效数值部分
    data[i]=data[i][2:11]
    if i%18==10:
        for j in range(9):
            data[i][j]=0.00001
    else:
        for j in range(9):
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

#print (data)
f=open("para.txt")

for i in range(7):
    w.append([])
i=0
for it in f:
    lis = it.split(' ')
    if i< 6:
        for s in lis[0:len(lis)-1]:
            w[i].append(float(s))
    else:
        w[i].append(float(lis[0]))
    i=i+1
def func(i,j):
    res=w[6][0]
    global datelen
    for k in range(6):
        for q in range(datelen):
            res=res+w[k][q]*data[k+i*6][j+q]
    if res<0:
        return 0
    return res

f = open("test_answer.txt",'w')

error = 0
f.write("date        expected PM2.5         actual PM2.5\n")
for i in range(240):
    F=func(i,9-datelen)
    f.write("id_"+str(i)+"     "+str(F)+"        "+str(data[2+i*6][8])+"\n")
    tem=F-data[2+i*6][8]
    error=error+tem**2
f.close()
print("误差为："+str(error/240))


