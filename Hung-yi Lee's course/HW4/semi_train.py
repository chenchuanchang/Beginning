# -*-coding:utf-8 -*-
# __author__=coco

import argparse, os

from keras import models
from keras.callbacks import EarlyStopping, ModelCheckpoint
from Datareader import DataReader
from RNN_model import RNN_model


parser = argparse.ArgumentParser(description='semi model')
parser.add_argument('--model_name',default='model/model_1.h5')
parser.add_argument('--action',default='semi_train')
parser.add_argument('--vocab_size',default=20000,type=int)

parser.add_argument('--result_path',default='result.csv')
parser.add_argument('--max_length',default=40,type=int)
parser.add_argument('--epoch',default=10,type=int)
parser.add_argument('--batch_size',default=100,type=int)
parser.add_argument('--loss_function',default='binary_crossentropy')
parser.add_argument('--threshold',default=0.3,type=float)

parser.add_argument('--load_model',default=True)

args = parser.parse_args()

semi_path='training_nolabel.txt'

def main():
    print('loading data...')
    da = DataReader()
    semi_x=da.read_data('semi_data',semi_path,False)

    print('getting Tokenizer')
    if not os.path.exists('semi_token.pk'):
        da.tokenize(args.vocab_size)
        da.save_tokenizer('semi_token.pk')
    else:
        da.load_tokenizer('semi_token.pk')

    da.to_sequence(args.max_length)

    model = models.load_model(args.model_name)
    print(model.summary())

    for i in range(args.epoch):
        semi_predict = model.predict(semi_x,batch_size=args.batch_size,verbose=True)
        semi_x,semi_y = da.get_semi_data('semi_data',semi_predict,args.threshold,args.loss_function)



if __name__ =='__main__':
    main()






