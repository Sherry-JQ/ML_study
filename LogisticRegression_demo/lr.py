#encoding:utf-8
'''
Create by shelly on 2016.9.8.
This is a demo for logistic regression.
The help from https://github.com/wepe/MachineLearning
'''
from numpy import *
from os import listdir
#代码里面用到python os模块里的listdir()，用于从文件夹里读取所有文件，返回的是列表(文件名)。
#python里的open()函数用于打开文件，之后用readline()一行行读取
def dataLoad(direction):
    datafilelist=listdir(direction)
    m=len(datafilelist)#m:simples' total numbers
    dataArray=zeros((m,1024)) #32*32=1024
    labelArray=zeros((m,1))
    #m个文件，获得每个文件的数据,形成m个[1,1024]的矩阵
    for i in range(m):
        returnArray=zeros((1,1024))
        filename=datafilelist[i]
        fr=open("%s/%s"%(direction,filename))#获取direction/目录下名为filename的文件
        for j in range(32):
            lineStr=fr.readline()#依次获取每个文件下每行的数据
            for k in range(32):
                returnArray[0,j*32+k]=int(lineStr[k])#每行中的32个数据依次读入

    dataArray[i,:]=returnArray
    labelArray[i]=int(filename.split('.')[0].split('_')[0])
    # filename0=filename.split('.')[0]#filename形如"1_20.txt",filename0=1_20
    # label=filename0.split('_')[0]#label=1
    # labelArray[i]=int(label)
    return dataArray,labelArray

def sigmoid(X):
    return 1.0/(1+exp(X))

#批梯度下降
def gradAscent(dataArray,labelArray,alpha,maxCycles):
    dataMat=mat(dataArray)#[m,n]
    labelMat=mat(labelArray)#[m,1]
    m,n=shape(dataMat)
    #一个数据的所有特征量的权重
    weights=ones((n,1))
    for i in range(maxCycles):
        weights=weights-alpha*dataMat.transpose()*(sigmoid(dataMat*weights)-labelMat)
    return weights

#随机梯度下降
def gradAscent2(dataArray,labelArray):
    alpha=0.07
    m,n=shape(dataArray)
    weights=ones(n)
    for i in range(m):
        weights=weights-alpha*(sigmoid(sum(dataArray[i]*weights))-labelArray[i])*dataArray[i]
    return weights

#以上用数据集train得出训练结果weights
#以下用训练结果weights检验数据集test的拟合程度
def classfy(testdirection,weights):
    dataArray,labelArray=dataLoad(testdirection)
    dataMat=mat(dataArray)#[m,n],m个数据，每个数据n个特征
    labelMat=mat(labelArray)#[m,1],记录真实标签
    m,n=shape(dataMat)
    h=sigmoid(dataMat*weights)#[m,1]=[m,n]*[n,1]
    error=0.0
    for i in range(m):
        if int(h[i])>0.5:
            print int(labelMat[i]),'is classfied as:1'
            if int(labelMat[i])!=1:
                error=error+1
                print "This is an error!"
        else:
            print int(labelMat[i]),'is classfied as:0'
            if int(labelMat[i])!=0:
                error=error+1
                print "This is an error!"
    print 'We find %d error:'%error
    print 'error rate is:','%.4f'%(error/m)

def digitRecognition(trainDir,testDir,alpha=0.07,maxCycles=10):
    data,label=dataLoad(trainDir)
    weight=gradAscent(data,label,alpha,maxCycles)
    classfy(testDir,weight)
def digitRecognition2(trainDir,testDir):
    data,label=dataLoad(trainDir)
    weight=gradAscent2(data,label)
    classfy(testDir,weight)
digitRecognition('train','test')