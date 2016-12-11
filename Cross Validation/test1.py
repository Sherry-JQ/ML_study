'''
Created by shelly about some ML algorithms on 2016.9.27.
Learn from http://blog.csdn.net/yangxudong/article/details/26869841.
'''
from sklearn import cross_validation
from sklearn import linear_model
from sklearn import tree
from sklearn import ensemble
from sklearn import svm

lr=linear_model.LogisticRegression()
lr_scores=cross_validation.cross_val_score(lr,train_data,train_target,cv=5)

