#encoding:utf-8
#a test for sklearn
import sklearn.datasets
import numpy as np
from sklearn import cross_validation
import random
# X=[[1,1,1],[0,-1,0],[0,0,0],[0,0,-2]]
# y=[1.,0.,0.,0.]
# model=svm.SVC()
# model.fit(X,y)
# print model.predict([[2,2,2],[-1,0,0]])
# print model.support_vectors_,model.support_,model.n_support_


################data##############
# iris=sklearn.datasets.load_iris()
# #random.shuffle(iris.data)---不能这样，data和target不对应了，必须用index
# #random.shuffle(iris.target)---不能这样，data和target不对应了，必须用index
# #print iris.target
# #print iris.data
# sampleRatio=0.7
# num_samples=len(iris.target)
# sampleBoundary=int(sampleRatio*num_samples)
#
# shuffleIndex=range(num_samples)
# #shuffleIndex=np.arange(num_samples)
# np.random.shuffle(shuffleIndex)
# #print shuffleIndex
# train_features=iris.data[shuffleIndex[:sampleBoundary]]
# train_labels=iris.target[shuffleIndex[:sampleBoundary]]
# test_features=iris.data[shuffleIndex[sampleBoundary:]]
# test_labels=iris.target[shuffleIndex[sampleBoundary:]]
# #train_features,test_features,train_labels,test_labels=cross_validation.train_test_split\
# #    (iris.data,iris.target,train_size=0.5,random_state=0)
# ############################################################
#
#
# ##########svm##########
# from sklearn import svm
# model=svm.SVC()
# model.fit(train_features,train_labels)
# predict_labels=model.predict(test_features)
# print predict_labels
# # count=0
# # for i in range(len(test_labels)):
# #     if predict_labels[i]==test_labels[i]:
# #         count+=1
# # accuracy=count*1.0/len(test_labels)
# # print accuracy
# #######################
#
# #########kMeans########
# # from sklearn.cluster import KMeans
# # model=KMeans(n_clusters=4)#default n_clusters=8
# # model.fit(train_features)
# # labels=model.labels_
# # print labels


###########OCR###########
digits=sklearn.datasets.load_digits()
import pylab as pl
# pl.gray()
# pl.matshow(digits.images[0])
# pl.show()
print digits.images[0]
print digits.data[0]