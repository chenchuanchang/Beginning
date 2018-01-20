# -*-coding:utf-8 -*-
# __author__=coco

import keras as ke
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np

number=60000

f=np.load("mnist.npz")
x_train,y_train = f['x_train'],f['y_train']
x_test,y_test = f['x_test'],f['y_test']

x_train= x_train.reshape(number,28*28)
x_test=x_test.reshape(x_test.shape[0],28*28)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

y_train = ke.utils.to_categorical(y_train, 10)
y_test = ke.utils.to_categorical(y_test, 10)

x_train /= 255
x_test /= 255

f.close()
print("载入完成")

model=ke.Sequential()
model.add(Dense(input_dim=28*28,units=500,activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(units=500,activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(units=10,activation='softmax'))
# model.add(Dropout(0.5))
model.compile(loss="categorical_crossentropy",
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=100,epochs=20)

score = model.evaluate(x_test,y_test)
print("总共的loss为："+str(score[0]))
print("准确度为："+str(score[1]))
model.save("model.h5")
#model = ke.models.load_model("model.h5")