#encoding=utf-8
'''
Created by Sherry on 2016.12.11.
This is a demo for SVM_SMO
The help is from the book "Machine Learning in Action"
'''
from numpy import *
from scipy import *
from sklearn import *
def loadData(filename):
    dataMat=[]
    labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):#i_alpha下标；m_alpha数目
    j=i
    #we want to select any J not equal to i
    while(j==i):
        j=int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])#if checks if an example violates KKT conditions
            if((labelMat[i]*Ei<-toler)and(alphas[i]<C)) or ((labelMat[i]*Ei>toler)and(alphas[i]>0)):
                j=selectJrand(i,m)
                fXj=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                Ej=fXj-float(labelMat[j])
                alphaIold=alphas[i].copy()
                alphaJold=alphas[j].copy()
                if(labelMat[i]!=labelMat[j]):
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,C+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-C)
                    H=min(C,alphas[j]+alphas[i])
                if L==H:
                    print "L==H"
                    continue
                eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-dataMatrix[i,:]*dataMatrix[i,:].T-dataMatrix[j,:]*dataMatrix[j,:].T
                if eta>=0:
                    print "eta>=0"
                    continue
                alphas[j]=alphas[j]-labelMat[j]*(Ei-Ej)/eta
                alphas[j]=clipAlpha(alphas[j],H,L)
                if(abs(alphas[j]-alphaJold)<0.00001):
                    print "j not moving enough"#此时就跳过下面的修改
                    continue
                alphas[i]=alphas[i]+labelMat[i]*labelMat[j]*(alphaJold-alphas[j])
                b1=b-Ei-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T\
                   -labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2=b-Ej-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T\
                   -labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (alphas[i]>0) and (alphas[i]<C):
                    b=b1
                elif (alphas[j]>0) and (alphas[j]<C):
                    b=b2
                else:
                    b=(b1+b2)/2.0
                alphaPairsChanged+=1
                print "iter: %d i:%d, pairs changed %d"%(iter,i,alphaPairsChanged)
        if (alphaPairsChanged==0):
            iter=iter+1
        else: iter=0
        print "iteration number: %d"%iter
    return b,alphas


dataArr,labelArr=loadData('testSet.txt')
bb,aa=smoSimple(dataArr,labelArr,0.6,0.001,40)