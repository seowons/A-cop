# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:40:57 2020

@author: sue
"""



from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
#from keras.models import load_model
#import cv2
import numpy as np
import matplotlib.pyplot as plt


categories = ["dumpling", "hotdog", "fishcake","laver", "pancake", "pasta", "spam", "tuna", "udon","rice"
              "ramen","chickensoup", "soup","tofusushi","tofu", "breast", "curry","duck", "jaban","peachcan"]
num_classes = len(categories)
# 학습 전용 데이터와 테스트 전용 데이터 구분 
X_train, X_test, Y_train, Y_test = np.load('C:\\Users\\user\\Desktop\\dataset\\img_data2.npy')
 
model = Sequential()
model = Sequential()
model.add(Convolution2D(16, 3, 3, border_mode='same', activation='relu',
                        input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Convolution2D(64, 3, 3,  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
 
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))


  
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=32, nb_epoch=500)


model.save('acop2.h5')
model.summary() #model.summary() 를 통해 모델의 대략적인 구조를 파악

X_train = np.append(X_train,X_test, axis=0)
Y_train = np.append(Y_train,Y_test, axis=0)
 
# Save Model with CheckPoint & StopPoint
from keras.callbacks import ModelCheckpoint,EarlyStopping
#import os
import datetime
 
Datetime = datetime.datetime.now().strftime('%m%d_%H%M')
modelpath="acop2.h5"
 
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='loss', patience=100)
 
# Learning and save models
history = model.fit(X_train, Y_train, validation_split=0.1, epochs=3500, batch_size=10, verbose=0, callbacks=[early_stopping_callback,checkpointer])

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

