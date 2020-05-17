# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 03:33:35 2020

@author: sue
"""


import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
 
categories = ["dumpling", "hotdog", "fishcake","laver", "pancake", "pasta", "spam", "tuna", "udon","rice"
              "ramen","chickensoup", "soup","tofusushi","tofu", "breast", "curry","duck", "jaban","peachcan"]

def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)
 
src = []
name = []
test = []
image_dir = "C:\\Users\\user\\Desktop\\test"
image_list = os.listdir(image_dir)

for file in image_list:
    if file.find('.jpg') is not -1 or file.find('.JPG') is not -1:      
        src.append(image_dir + file)
        name.append(file)
        test.append(Dataization(image_dir + '\\' + file))
        print(test)
 
test = np.array(test)
print(test)
model = load_model('acop2.h5')
predict = model.predict_classes(test)
 
for i in range(len(test)):
    print(name[i] + " : , Predict : "+ str(categories[predict[i]]))


