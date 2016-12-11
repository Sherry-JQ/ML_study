#encoding:utf-8
'''
Created by Sherry on 2016.12.11.
This is a demo for k_means.
The help is from http://blog.csdn.net/lipengcn/article/details/50320893
'''
from numpy import *
def loadDataSet(filename):
    dataMat=[]
    fr=open(filename)
    for perline in fr.readlines():
        curLine=perline.strip().split('\t')
        fltLine=map(float,curLine) #将数据转换成float型
        dataMat.append(fltLine)
    return mat(dataMat)

def distEclud(vecA,vecB):#两质心之间的欧几里得距离
    return sqrt(sum(power(vecA-vecB,2))) #差、平方、求和

def randCent(dataSet,k): #构建含k个随机质心的集合
    n=shape(dataSet)[1] #列的维数，表示每个质点的n个参数
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids

def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))#两列，第一列记录index，第二列记录误差
    kMcentroids=createCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):#第i个数据点
            minDist=inf
            minIndex=-1
            for j in range(k):#第j个质心点
                distJI=distMeas(kMcentroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI
                    minIndex=j
            if clusterAssment[i,0]!=minIndex:#只要i个数据点中有至少一个的minIndex变化了，就不收敛，，收敛时会出现重复
                 clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        print kMcentroids#初代质心集，二代质心集，...，直到收敛的末代
        for cent in range(k):
            #nonzeros(a)返回数组a中值不为零的元素的下标[][]...[]
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#找到以cent为质心的小数据集
            kMcentroids[cent,:] = mean(ptsInClust, axis=0)#计算刚刚得到的小数据集的所有点的均值，更新质心，axis=0表示按列计算
    return kMcentroids, clusterAssment



loadDataMat=loadDataSet('testSet.txt')
mycentroids,myclustAss=kMeans(loadDataMat,4)

