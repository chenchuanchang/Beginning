# -*-coding:utf-8 -*-
# __author__=coco

#文本划分和计数
count={}

for s in open("words.txt"):
    s_lump = s[0:len(s)-1].split(' ')
    for x in s_lump:
        if (x in count):
            count[x]=count[x]+1
        else :
            count[x]=1
cnt=0
with open("answer.txt",'w') as f:
    for x in count:
        f.write("%s %d %d\n" %(x,cnt,count[x]))
        cnt=cnt+1
