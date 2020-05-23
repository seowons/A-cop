# -*- coding: utf-8 -*-
"""
Created on Thu May 21 04:29:45 2020

@author: sue
"""
import numpy as np
from keras.models import load_model

categories = ["dumpling", "hotdog", "fishcake","laver", "pancake", "pasta", "spam", "tuna", "udon","rice"
              "ramen","chickensoup", "soup","tofusushi","tofu", "breast", "curry","duck", "jaban","peachcan"]
num_classes = len(categories)

X_train, X_test, Y_train, Y_test = np.load('C:\\Users\\user\\Desktop\\dataset\\img_data2.npy')

X_train = np.append(X_train,X_test, axis=0)
Y_train = np.append(Y_train,Y_test, axis=0)
 
model = load_model("acop3.h5")

# Save Model with CheckPoint & StopPoint
from keras.callbacks import ModelCheckpoint,EarlyStopping
#import os
import datetime
 
Datetime = datetime.datetime.now().strftime('%m%d_%H%M')
modelpath="acop3.h5"
 
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='loss', patience=100)
 
# Learning and save models
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=3500, batch_size=10, verbose=0, callbacks=[early_stopping_callback,checkpointer])

import matplotlib.pylab as plt
print(history.history.keys())

print(history.history['accuracy']) 
# acc: 매 epoch 마다의 훈련 정확도
print(history.history['loss']) 
#loss:매 epoch 마다의 훈련 손실 값
print(history.history['val_accuracy'])
# val_acc매 epoch 마다의 검증 정확도
print(history.history['val_loss'])
# val_loss 매 epoch마다의 검증 손실 값

## summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
## summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()