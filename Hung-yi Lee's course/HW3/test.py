# -*-coding:utf-8 -*-
# __author__=coco
# from cnn_simple import build_model
from utils import *
import pickle_model as pm
import os
import numpy as np
import argparse
import time
from keras import models

test_pixels,test_labels = pm.test_data()

for i in range(len(test_labels)):
    test_pixels[i] = np.array(test_pixels[i]).reshape((48, 48, 1))
    onehot = np.zeros((7, ), dtype=np.float)
    onehot[int(test_labels[i])] = 1.
    test_labels[i] = onehot

model = models.load_model('model/nn-model-1.h5')
score = model.evaluate(np.asarray(test_pixels),np.asarray(test_labels))
print("总共的loss为："+str(score[0]))
print("准确度为："+str(score[1]))