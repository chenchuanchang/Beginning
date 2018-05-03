# -*-coding:utf-8 -*-
# __author__=coco

import  argparse, os
import numpy as np

from keras import models
from keras.callbacks import EarlyStopping, ModelCheckpoint
from Datareader import DataReader
from RNN_model import RNN_model

parser = argparse.ArgumentParser(description='RNN model')
parser.add_argument('--model_name',default='model/model_1.h5')
parser.add_argument('--action',default='train')

# training argument
parser.add_argument('--batch_size',default=100,type=int)
parser.add_argument('--epoch',default=100000,type=int)
parser.add_argument('--val_rate',default=0.2,type=float)
parser.add_argument('--vocab_size',default=20000,type=int)
parser.add_argument('--max_length',default=40,type=int)

# model parameter
parser.add_argument('--loss_function',default='binary_crossentropy')
parser.add_argument('--cell',default='LSTM',choices=['LSTM','GRU'])
parser.add_argument('--emb_dim',default=128,type=int)
parser.add_argument('--hid_size',default=512,type=int)
parser.add_argument('--dropout_rate',default=0.5,type=float)

parser.add_argument('--result_path',default='result.csv')

parser.add_argument('--load_model',default=False)

args = parser.parse_args()

train_path='training_label.txt'

def main():
    print('loading data...')
    da = DataReader()
    da.read_data('train_data',train_path,True)

    print('getting Tokenizer')
    if not os.path.exists('token.pk'):
        da.tokenize(args.vocab_size)
        da.save_tokenizer('token.pk')
    else:
        da.load_tokenizer('token.pk')

    da.to_sequence(args.max_length)

    if args.load_model ==True:
        model = models.load_model(args.model_name)
    else:
        model = RNN_model(args)
    print(model.summary())

    (x,y),(x_val,y_val) = da.split_data('train_data',args.val_rate)
    earlystopping = EarlyStopping(monitor='val_acc',patience=10,verbose=1,mode='max')
    checkpoint = ModelCheckpoint(filepath=args.model_name,
                                 verbose=1,
                                 save_best_only=True,
                                 save_weights_only=False,
                                 monitor='val_acc',
                                 mode='max')

    result = model.fit(x,y,validation_data=(x_val,y_val),
                       epochs=args.epoch,
                       batch_size=args.batch_size,
                       callbacks=[checkpoint,earlystopping])



if __name__ =='__main__':
    main()






