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
    '''
    先來看一下keras document 的Conv2D
    keras.layers.Conv2D(filters, kernel_size, strides=(1, 1),
        padding='valid', data_format=None, dilation_rate=(1, 1),
        activation=None, use_bias=True, kernel_initializer='glorot_uniform',
        bias_initializer='zeros', kernel_regularizer=None,
        bias_regularizer=None, activity_regularizer=None,
        kernel_constraint=None, bias_constraint=None)
    '''
    block1 = Conv2D(64, (3, 3), padding='valid', activation='relu')(input_img)
    block1 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block1)
    block1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block1)
    # block1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block1)
    # block1 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block1)
    #
    block2 = Conv2D(64, (3, 3), padding='valid',activation='relu')(block1)
    block2 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block2)
    # block2 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block2)
    # #
    block3 = Conv2D(128, (3, 3), padding='valid',activation='relu')(block2)
    block3 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block3)
    block3 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block3)
    # # #
    block4 = Conv2D(128, (3, 3), padding='valid',activation='relu')(block3)
    block4 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block4)
    # block4 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block4)
    # #
    # block5 = Conv2D(128, (3, 3), activation='relu')(block4)
    # block5 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block5)
    # block5 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block5)
    # #
    # block6 = Conv2D(128, (3, 3), activation='relu')(block5)
    # # block6 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(block6)
    # block6 = ZeroPadding2D(padding=(1, 1), data_format='channels_last')(block6)

    block6 = Flatten()(block4)
    #
    # fc1 = Dense(32, activation='relu')(block6)
    # fc1 = Dropout(0.5)(fc1)
    #
    # fc2 = Dense(500, activation='relu')(fc1)
    # fc2 = Dropout(0.5)(fc2)
    #
    # fc3 = Dense(256, activation='relu')(fc2)
    # fc1 = Dropout(0.5)(fc1)
    #
    # fc4 = Dense(500, activation='relu')(fc3)
    # fc1 = Dropout(0.5)(fc1)
    #
    # fc5 = Dense(500, activation='relu')(fc4)
    # fc1 = Dropout(0.5)(fc1)

    predict = Dense(7)(block6)
    predict = Activation('softmax')(predict)
    model = Model(inputs=input_img, outputs=predict)

    # opt = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    opt = Adam(lr=1e-3)
    # opt = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    model.summary()
    return model