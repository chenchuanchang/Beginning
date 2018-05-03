# -*-coding:utf-8 -*-
# __author__=coco

import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import _pickle as pk

class DataReader:
    def __init__(self):
        self.data={}

    def read_data(self,name,data_path,with_label=True):
        print("read data from %s  "%data_path)
        x, y=[],[]
        f = open('training_label.txt',errors='ignore')
        for line in f:
            if with_label:
                lines = line.strip().replace(" +++$+++ ","&").split("&")
                x.append(lines[1])
                # print(lines[0])
                try:
                    y.append(int(lines[0]))
                except:
                    y.append(int(lines[0][1]))
            else:
                x.append(line)
        if with_label:
            self.data[name]=[x,y]
        else:
            self.data[name]=[x]

    def tokenize(self,vocab_size):
        print("create new tokenizer")
        self.tokenizer = Tokenizer(num_words=vocab_size)
        for key in self.data:
            print("tokenizing %s"%key)
            texts = self.data[key][0]
            self.tokenizer.fit_on_texts(texts)

    def save_tokenizer(self,path):
        print("save tokenizer to %s"%path)
        pk.dump(self.tokenizer,open(path,'wb'))

    def load_tokenizer(self,path):
        print("Load tokenizer from %s"%path)
        self.tokenizer = pk.load(open(path,'rb'))

    def to_sequence(self,maxlen):
        self.maxlen=maxlen
        for key in self.data:
            print('Converting %s to sequences'%key)
            tmp = self.tokenizer.texts_to_sequences(self.data[key][0])
            # print(tmp)
            self.data[key][0]=np.array(pad_sequences(tmp,maxlen=maxlen))
            # print(self.data[key][0])

    def to_bow(self):
        for key in self.data:
            print ('Converting %s to tfidf'%key)
            self.data[key][0] = self.tokenizer.texts_to_matrix(self.data[key][0],mode='count')


    def to_category(self):
        for key in self.data:
            if len(self.data[key]) == 2:
                self.data[key][1] = np.array(to_categorical(self.data[key][1]))

    def get_semi_data(self,name,label,threshold,loss_function):
        # th is the gate to pick label>th
        label = np.squeeze(label)
        semi_data=[]
        semi_label=[]
        for i in range(0,len(label)):
            if label<threshold or label >(1-threshold):
                semi_data.append(self.data[name][0][i])
                semi_label.append(label[i])
        return semi_data,semi_label

    def get_data(self,name):
        return self.data[name][0]

    def split_data(self,name,rate):
        data = self.data[name]
        X = data[0]
        Y = data[1]
        data_size = len(X)
        val_size = int(data_size * rate)
        return (X[val_size:],Y[val_size:]),(X[:val_size],Y[:val_size])

