# -*-coding:utf-8 -*-
# __author__=coco


from keras.models import Model
from keras.layers import Input, GRU, LSTM, Dense
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam

def RNN_model(args):
    inputs = Input(shape=(args.max_length,))

    embedding = Embedding(args.vocab_size,args.emb_dim,trainable=True)(inputs)

    if args.cell == 'LSTM':
        RNN_cell = LSTM(args.hid_size,return_sequences=False,dropout=args.dropout_rate)
    elif args.cell=='GRU':
        RNN_cell = GRU(args.hid_size,return_sequences=False,dropout=args.dropout_rate)

    RNN_output = RNN_cell(embedding)

    outputs = Dense(1,activation='sigmoid')(RNN_output)

    model =  Model(inputs=inputs,outputs=outputs)

    adam = Adam()

    model.compile(loss=args.loss_function,optimizer=adam,metrics=['accuracy'])

    return model
