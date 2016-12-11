'''
Created by Sherry on 2016.10.7 for Hog and perceptron.
Help from http://blog.csdn.net/wds2006sdo/article/details/51923546.
'''
#encoding:utf-8
import pandas as pd
import numpy as np
import cv2
import time
import random
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

study_step = 0.0001                                 # 学习步长
study_total = 10000                                 # 学习次数
feature_length = 324                                # hog特征维度  ???
object_num = 0                                      # 分类的数字

def get_hog_features(trainSet):
    features=[]
    hog=cv2.HOGDescriptor('./hog.xml')
    for img in trainSet:
        img=np.reshape(img,(28,28))
        cv_img=img.astype(np.uint8)

        hog_feature=hog.compute(cv_img)
        features.append(hog_feature)

    features=np.array(features)
    features=np.reshape(features,(-1,324))
    return features

def train(trainSet,train_labels):
    trainSet_size=len(train_labels)
    w=np.zeros((feature_length,1))
    b=0

    study_count=0
    noChange_count=0
    noChange_upper_limit=100000

    while True:
        noChange_count+=1
        if noChange_count>noChange_upper_limit:
            break

        #random for data
        index=random.randint(0,trainSet_size-1)
        img=trainSet[index]
        label=train_labels[index]



