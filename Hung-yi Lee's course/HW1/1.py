# -*-coding:utf-8 -*-
# __author__=coco
import csv

reader=csv.reader(open('train.csv', encoding='gbk',errors="ignore"))
for item in reader:
    print(item)