# -*-coding:utf-8 -*-
# __author__=coco

import pickle

def train_data():
    train_pixels=[]
    train_labels=[]
    valid_pixels=[]
    valid_labels=[]
    count = 0
    with open('train.csv', 'r') as f:
        f.readline()
        for i, line in enumerate(f):
            count = count+1
            # print(line)
            data = line.split(',')
            label = int(data[0])
            pixel = [float(x)/255 for x in data[1].split(' ')]
            # print (pixel)
            # if count >20000:
            #     break
            if count%4!=0:
                train_labels.append(label)
                train_pixels.append(pixel)
            else:
                valid_labels.append(label)
                valid_pixels.append(pixel)
    # print(len(train_labels))
    return train_pixels,train_labels,valid_pixels,valid_labels

def test_data():
    test_pixels=[]
    test_labels=[]
    with open('train.csv', 'r') as f:
        f.readline()
        for i, line in enumerate(f):
            data = line.split(',')
            label = int(data[0])
            pixel = [float(x)/255 for x in data[1].split(' ')]
            test_labels.append(label)
            test_pixels.append(pixel)
    # print(len(train_labels))
    # print(test_labels)
    return test_pixels,test_labels
# test_data()