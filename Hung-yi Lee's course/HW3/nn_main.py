# -*-coding:utf-8 -*-
# __author__=coco

from nn_simple import build_model
from utils import *
import pickle_model as pm
import os
import numpy as np
import argparse
import time
from keras import models

os.system('echo $CUDA_VISIBLE_DEVICES')
PATIENCE = 5 # The parameter is used for early stopping

def main():
    parser = argparse.ArgumentParser(prog='train.py')
    parser.add_argument('--epoch', type=int, default=100)
    parser.add_argument('--batch', type=int, default=99)
    parser.add_argument('--pretrain', type=bool, default=False)
    parser.add_argument('--save_every', type=int, default=2)
    parser.add_argument('--model_name', type=str, default='model/model-1')
    args = parser.parse_args()

    # training data
    train_pixels,train_labels,valid_pixels,valid_labels=pm.train_data()
    print ('# of training instances: ' + str(len(train_labels)))
    # validation data
    print ('# of validation instances: ' + str(len(valid_labels)))

    for i in range(len(valid_labels)):
        valid_pixels[i] = np.array(valid_pixels[i]).reshape((48, 48, 1))
        onehot = np.zeros((7, ), dtype=np.float)
        onehot[int(valid_labels[i])] = 1.
        valid_labels[i] = onehot

    # start training
    train(args.batch, args.epoch, args.pretrain, args.save_every,
          train_pixels, train_labels,
          np.asarray(valid_pixels), np.asarray(valid_labels),
          args.model_name)

def train(batch_size, num_epoch, pretrain, save_every, train_pixels, train_labels, val_pixels, val_labels, model_name=None):

    if pretrain == False:
        model = build_model()
    else:
        model = models.load_model(model_name)

    Y_batch = []
    for n in range(len(train_labels)):
        Y_batch.append(np.zeros((7, ), dtype=np.float))
        train_pixels[n] = np.array(train_pixels[n]).reshape((48, 48, 1))
        # print(type(X_batch[-1]))
        Y_batch[n][int(train_labels[n])] = 1.
    best=0
    for n in range(num_epoch):
        model.fit(np.asarray(train_pixels),np.asarray(Y_batch),batch_size=200,epochs=1)
        loss_and_metrics = model.evaluate(val_pixels, val_labels)
        if loss_and_metrics[1]>best:
            best=loss_and_metrics[1]
            model.save('model/nn-model-1.h5')
        print ('总共第%d epoch'%(n+1))
        print ('\nloss & metrics:')
        print (loss_and_metrics)
        print ('\n历史最好为：')
        print (best)

if __name__=='__main__':
    main()