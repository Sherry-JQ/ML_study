#encoding:utf-8
'''
Created by Shelly on 2016.9.11.
This is a demo for Naive Bayes.
The help is from http://blog.csdn.net/lipengcn/article/details/49496107
'''
from numpy import *
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]   # 0 for normal, 1 for insult
    return postingList, classVec


### preparing data ###
# create a vocablary list for dataSet
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# set-of-words model
def setOfWords2Vec(vocabList, inputSet):
    # the inputSet refers to a new input document as same in dataSet
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocablary!" % word
    return returnVec



### training ###
def trainNBO(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs) #类别为“1”的P（yk）（此例中类别记为0和1）
    p0Num = ones(numWords) # bayes evaluation
    p1Num = ones(numWords) # bayes evaluation #是类别为yk的样本中，第i维特征的值是xi的样本个数，
    p0Denom = 2.0 # bayes evaluation
    p1Denom = 2.0 # bayes evaluation #类别为“1”的样本个数
    for ii in range(numTrainDocs):
        if trainCategory[ii] == 1:
            p1Num += trainMatrix[ii]
            p1Denom += sum(trainMatrix[ii])
        else:
            p0Num += trainMatrix[ii]
            p0Denom += sum(trainMatrix[ii])
    p1Vect = log(p1Num/p1Denom) # avoiding the underflow
    p0Vect = log(p0Num/p0Denom) # avoiding the underflow
    return p0Vect, p1Vect, pAbusive


### testing ###
# classifying
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0
def testingNB():
    loadList,loadClassVec=loadDataSet()
    listVab=createVocabList(loadList)
    trainMat=[]
    for Doc in loadList:
        trainMat.append(setOfWords2Vec(listVab,Doc))
    p0v,p1v,pAb=trainNBO(trainMat,loadClassVec)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc=array(setOfWords2Vec(listVab,testEntry))
    print testEntry, 'classfied as: ', classifyNB(thisDoc, p0v, p1v, pAb)
testingNB()

