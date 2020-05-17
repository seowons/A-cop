# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:26:57 2020

@author: sue
"""


import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
  
groups_folder_path = 'C:\\Users\\user\\Desktop\\dataset\\'
categories = ["dumpling", "hotdog", "fishcake","laver", "pancake", "pasta", "spam", "tuna", "udon","rice"
              "ramen","chickensoup", "soup","tofusushi","tofu", "breast", "curry","duck", "jaban","peachcan"]
 
num_classes = len(categories)


image_w = 28
image_h = 28
  
X = []
Y = []

for index, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[index] = 1
    image_dir = groups_folder_path + categorie + '/'
  
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir+filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
            X.append(img/256) #픽셀 0~255값을 가짐 학습하려면 0~1사이의 소수가 필요그래서 256으로 나눔..
            Y.append(label)#
 
X = np.array(X)
Y = np.array(Y)
 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)
 
np.save("C:\\Users\\user\\Desktop\\dataset\\img_data2.npy", xy)
