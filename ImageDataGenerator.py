# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:19:59 2020

@author: sue
"""

from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

img = load_img('C:\\Users\\user\\Desktop\\test1\\udon (1).jpg')  # PIL 이미지
x = img_to_array(img)  # (3, 150, 150) 크기의 NumPy 배열
x = x.reshape((1,) + x.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열


# 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
#C:\\Users\\user\\Desktop\\test1\\preview 에 저장
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='C:\\Users\\user\\Desktop\\test1\\preview', save_prefix='udon', save_format='jpeg'):
    i += 1
    if i > 20:
        break  # 이미지 20장을 생성하고 마칩니다

        
