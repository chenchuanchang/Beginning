# -*-coding:utf-8 -*-
# __author__=coco

import os
import tensorflow as tf
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import _pickle as pk

f = open('training_label.txt',errors='ignore')
print(f)
line = f.readline()
print(line)

