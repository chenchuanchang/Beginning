# -*-coding:utf-8 -*-
# __author__=coco

from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten, Activation, Reshape
from keras.layers.convolutional import Conv2D, ZeroPadding2D
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.optimizers import SGD, Adam, Adadelta

def build_model():

    '''
    #先定義好框架
    #第一步從input吃起
    '''
    input_img = Input(shape=(48, 48, 1))

    block = Flatten()(input_img)
    #
    fc1 = Dense(500, activation='relu')(block)
    fc1 = Dropout(0.5)(fc1)
    #
    fc2 = Dense(1000, activation='relu')(fc1)
    fc2 = Dropout(0.5)(fc2)
    #
    fc3 = Dense(1000, activation='relu')(fc2)
    fc3 = Dropout(0.5)(fc3)
    #
    # fc4 = Dense(500, activation='relu')(fc3)
    # fc4 = Dropout(0.5)(fc4)
    #
    # fc5 = Dense(500, activation='relu')(fc4)
    # fc5 = Dropout(0.5)(fc1)

    predict = Dense(7)(fc3)
    predict = Activation('softmax')(predict)
    model = Model(inputs=input_img, outputs=predict)

    # opt = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    opt = Adam(lr=1e-3)
    # opt = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    model.summary()
    return model