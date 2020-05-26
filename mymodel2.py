import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import keras.losses
import consts as cnst
import matplotlib.pyplot as plt

np.random.seed(3)

input_shape = cnst.IMG_ROWS, cnst.IMG_COLS, 3

#데이터 생성

train_datagen = ImageDataGenerator(rescale = 1./255) #이미지 픽셀 값을 0~1 값으로 맞춰주기 위해

train_generator = train_datagen.flow_from_directory(
    'dataset/train_set',
    target_size = (24,24),
    batch_size = 5,
    class_mode = 'categorical')

test_datagen = ImageDataGenerator(rescale = 1./255)

test_generator = test_datagen.flow_from_directory(
    'dataset/test_set',
    target_size = (24,24),
    batch_size = 5,
    class_mode = 'categorical')

#모델 구성
model = Sequential()
model.add(Conv2D(16, kernel_size=(3, 3), padding = "same", activation = 'relu', input_shape = input_shape))
model.add(MaxPooling2D(pool_size = (2, 2), strides = (2, 2), padding = "same"))
model.add(Dropout(0.25))

model.add(Conv2D(64, kernel_size=(3, 3), padding = "same", activation = 'relu', input_shape = input_shape))
model.add(MaxPooling2D(pool_size = (2, 2), strides = (2, 2), padding = "same"))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256,activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(cnst.N_CLASSES,activation = 'softmax'))


#모델 학습과정 설정 
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ["accuracy"]) #다중 클래스, 최적화 알고리즘, 평가척도 

model.fit_generator(
    train_generator,
    steps_per_epoch = 15,
    epochs = 50,
    validation_data = test_generator,
    validation_steps = 5)

print("--Evaluate --")
scores = model.evaluate_generator(test_generator,steps = 5)
print("%s : %.4f%%" %(model.metrics_names[1], scores[1]*100))

print("--Predict --")
output = model.predict_generator(test_generator, steps =5)
np.set_printoptions(formatter={'float':lambda x:"{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)

hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10, validation_data=(X_val, Y_val))

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['acc'], 'b', label='train acc')
acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
      
    


