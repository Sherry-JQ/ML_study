#encoding:utf-8

#import pandas as pd
import csv
import sklearn.cross_validation as cross_validation
from sklearn import neighbors
import sklearn.metrics as metrics

csvfile=open(r'train.csv','rb')
reader=csv.reader(csvfile)
headers=reader.next()
print headers

featureList=[]
labelList=[]
for row in reader:
    labelList.append(row[0])
    featureList.append(row[1:])
print featureList