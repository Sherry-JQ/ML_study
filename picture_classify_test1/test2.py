#encoding=utf-8
'''
Created by Sherry for KNN and OCR on 2016.10.13
'''
import cv2
import numpy as np
img=cv2.imread('digits.png')
grayImg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#有 5000 个手写数字（每个数字重复 500遍）。每个数字是一个 20x20 的小图。
cells=[np.hsplit(row,100)for row in np.vsplit(grayImg,50)]#5000个
x=np.array(cells)
#我们使用每个数字的前 250 个样本做训练数据，剩余的250做测试数据。
train=x[:,:50].reshape(-1,400).astype(np.float32)#400=20*20每个像素点作为特征
test=x[:,50:100].reshape(-1,400).astype(np.float32)

k=np.arange(10)
train_labels=np.repeat(k,250)[:,np.newaxis]
test_labels=train_labels.copy()

print x[:,:50]
# knn=cv2.KNearest()
# knn.train(train,train_labels)
# ret,result,neighbours,dist=knn.find_nearest(test,k=5)
#
# matches=result==test_labels
# correct=np.count_nonzero(matches)
# accuracy=correct*100.0/result.size
# print accuracy


# def knn_classifier(train_x, train_y):
#     from sklearn.neighbors import KNeighborsClassifier
#     model = KNeighborsClassifier()
#     model.fit(train_x, train_y)
#     return model


# def knn_Classify(trainData,trainLabel,testData):
#     from sklearn.neighbors import KNeighborsClassifier
#     knnClf=KNeighborsClassifier()
#     knnClf.fit(trainData,trainLabel)
#     testLabel=knnClf.predict(testData)
#     return  testLabel
# tL=knn_Classify(train,train_labels,test)
# matches=tL==test_labels
# correct=np.count_nonzero(matches)
# accuracy=correct*100.0/tL.size
# print accuracy