# -*- coding: utf-8 -*-
"""
Created on Thu May 21 02:50:54 2020

@author: sue
"""



from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, MaxPooling2D
#from keras.models import load_model
#import cv2
import numpy as np
from keras.layers import Conv2D
 
categories = ["dumpling", "hotdog", "fishcake","laver", "pancake", "pasta", "spam", "tuna", "udon","rice"
              "ramen","chickensoup", "soup","tofusushi","tofu", "breast", "curry","duck", "jaban","peachcan"]
num_classes = len(categories)

X_train, X_test, Y_train, Y_test = np.load('C:\\Users\\user\\Desktop\\dataset\\img_data2.npy')
 
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=X_train.shape[1:], padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 전결합층
model.add(Flatten())    # 벡터형태로 reshape
model.add(Dense(512))   # 출력
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(num_classes))
model.add(Activation('softmax'))
# 모델 구축하기
model.compile(loss='categorical_crossentropy',   # 최적화 함수 지정
    optimizer='rmsprop',
    metrics=['accuracy'])



history=model.fit(X_train, Y_train, batch_size=32, nb_epoch=50)
 
model.save('acop4.h5')

print(history.history.keys())
print(history.history['accuracy']) 
# acc: 매 epoch 마다의 훈련 정확도
print(history.history['loss']) 


import matplotlib.pylab as plt
# list all data in history
print(history.history.keys())

print(history.history['accuracy']) 
# acc: 매 epoch 마다의 훈련 정확도
print(history.history['loss']) 
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])


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
history = model.fit(X_train, Y_train, validation_split=0.3, epochs=500, batch_size=10, verbose=0, callbacks=[early_stopping_callback,checkpointer])


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
