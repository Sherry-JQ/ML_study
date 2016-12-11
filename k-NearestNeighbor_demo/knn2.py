#encoding:utf-8
'''
Create by shelly on 2016.12.9.
This is a demo for KNN.
The help from https://github.com/wepe/MachineLearning
'''
from numpy import *
from os import listdir
import operator

def classfy0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] #shape[0]得出dataSet的行数，即样本个数
    diffSet=tile(inX,(dataSetSize,1))-dataSet#有一种数据copy m行的效果
    aqDiffMat=diffSet**2
    sqDistances=aqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndex=distances.argsort()
    classCount={}
    for i in range(k):
        voteLabel=labels[sortedDistIndex[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1

    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def readTest(filename):
    inputdata=zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        perlinedata=fr.readline()
        for j in range(32):
            inputdata[0,i*32+j]=int(perlinedata[j])
    return inputdata

def trainingData():
    traintextNameList=listdir('trainingDigits')
    m=len(traintextNameList)
    dataArray=zeros((m,1024))
    labelArray=[]
    for i in range(m):
        mylabel=int(traintextNameList[i].split('.')[0].split('_')[0])
        labelArray.append(mylabel)
        dataArray[i,:]=readTest('trainingDigits/%s'%(traintextNameList[i]))

    testtextNameList=listdir('testDigits')
    m2=len(testtextNameList)
    errorNum=0.0
    for j in range(m2):
        testDataArray=readTest('testDigits/%s'%(testtextNameList[j]))
        testLabel=int(testtextNameList[j].split('.')[0].split('_')[0])
        classfyResult=classfy0(testDataArray,dataArray,labelArray,3)
        print "the classifier came back with: %d, the real answer is: %d" % (classfyResult, testLabel)
        if(classfyResult!=testLabel):
            errorNum+=1.0
    print "\nthe total number of errors is: %d" % errorNum
    print "\nthe total error rate is: %f" % (errorNum/float(m2))


trainingData()
