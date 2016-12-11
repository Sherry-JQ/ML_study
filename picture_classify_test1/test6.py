#encoding=utf-8
'''
Created by Sherry on 2016.10.16
Histogram and Kmeans、SVM
'''
import cv2
import numpy as np
from sklearn import preprocessing
from sklearn import decomposition
############SIFT(&PCA)###########
def siftFeature(imgPath):
    img=cv2.imread(imgPath)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift=cv2.SIFT()
    kp=sift.detect(img_gray,None) # kp 是所有128特征描述子的集合
    kp,des=sift.compute(img_gray,kp) # kp 特征点的描述符; des 特征点个数*128维的矩阵
    des=preprocessing.normalize(des)
    #des=preprocessing.scale(des)
    #des=cv2.normalize(des)
    des=des.T
    print des.shape
    pca=decomposition.PCA(n_components=6)
    des=pca.fit_transform(des)
    des=des.flatten()
    #des=des.ravel()
    return des
###############SURF###############
def surfFeatures(imgPath):
    img=cv2.imread(imgPath)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    surf=cv2.SURF(2000)
    # brief=cv2.DescriptorExtractor_create("BRIEF")
    # kp=brief.detect(img_gray,None)
    kp=surf.detect(img_gray,None)
    kp,des=surf.compute(img_gray,kp)
    pca=decomposition.PCA(n_components=1)
    des=preprocessing.normalize(des)
    des=des.T
    #print des.shape
    des=pca.fit_transform(des)
    des=des.ravel()
    # print newdata.shape
    return des


    # kp,des=surf.detectAndCompute(img_gray,None)
    # des=cv2.normalize(des)
    # arrayDes=[]
    # n=des.shape[0]
    # print n
    # for i in range(n):
    #     arrayDes.extend(des[i])
    # return arrayDes

##########this histogram with no mask and 3 channel for RGB(cv2--BGR)
def histogram_0(imgPath):
    img=cv2.imread(imgPath)
    color=[(255,0,0),(0,255,0),(0,0,255)]
    arrayHist=[]
    for chan,col in enumerate(color):
        hist=cv2.calcHist([img],[chan],None,[256],[0.0,255.0])
        hist=cv2.normalize(hist).flatten()
        arrayHist.extend(hist)
    return arrayHist

###########this histogram with 5 masks and 3 channel for HSV
def histogram_1(imgPath):
    img=cv2.imread(imgPath)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    arrayHist=[]
    bins=(6,9,2)
    (h,w)=img.shape[:2]
    (cX,cY)=(int(w*0.5),int(h*0.5))
    segments=[(0,0,cX,cY),(cX,0,w,cY),(cX,cY,w,h),(0,cY,cX,h)]
    (axesX,axesY)=(int(w*0.75)/2,int(h*0.75)/2)
    ellipMask=np.zeros(img.shape[:2],dtype='uint8')
    cv2.ellipse(ellipMask,(cX,cY),(axesX,axesY),0,0,360,255,-1)
    for(startX,startY,endX,endY)in segments:
        cornerMask=np.zeros(img.shape[:2],dtype='uint8')
        cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
        cornerMask=cv2.subtract(cornerMask,ellipMask)
        hist=cv2.calcHist([img],[0,1,2],mask=cornerMask,histSize=bins,ranges=[0,180,0,256,0,256])
        #hist=cv2.calcHist([img],[0,1,2],cornerMask,bins,[0,180,0,256,0,256])
        hist=cv2.normalize(hist).flatten()
        arrayHist.extend(hist)

    hist=cv2.calcHist([img],[0,1,2],mask=ellipMask,histSize=bins,ranges=[0,180,0,256,0,256])
    hist=cv2.normalize(hist).flatten()
    arrayHist.append(hist)
    return arrayHist

def cornerHarrris(imgPath):
    img=cv2.imread(imgPath)
    img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #img_gray=np.float32(img_gray)
    dst=cv2.cornerHarris(img_gray,2,3,0.04)
    pca=decomposition.PCA(n_components=5)
    dst=preprocessing.normalize(dst)
    dst=dst.T
    #print dst.shape
    dst=pca.fit_transform(dst)
    dst=dst.ravel()
    #print len(dst),dst.shape
    return dst

def starbrief(imgPath):
    img=cv2.imread(imgPath)
    img=np.float32(img)
    star=cv2.FeatureDetector_create('STAR')
    brief=cv2.DescriptorExtractor_create('BRIEF')
    kp=star.detect(img,None)
    kp,des=brief.compute(img,kp)
    des=preprocessing.normalize(des)
    des=des.T
    print des.shape
    pca=decomposition.PCA(n_components=4)
    des=pca.fit_transform(des)
    des=des.ravel()
    print des.shape
    return des
starbrief('E:\\picture\\ml\\vacation-image-search-engine\\ss\\100100.png')
starbrief('E:\\picture\\ml\\vacation-image-search-engine\\ss\\100000.png')
def obg(imgPath):
    img=cv2.imread(imgPath)
#########load picture#########
from os import listdir
def loadImg(direction):
    List=listdir(direction)
    imgIndexList=[]
    m=len(List)
    for i in range(m):
        imgIndexList.append(direction+'\\'+List[i])
    return imgIndexList

########get feature(total)###
# def getFeature(imgIndexList):
#     m=len(imgIndexList)
#     features=[]
#     for i in range(m):
#         #arrayHist=histogram_0(imgIndexList[i])
#         #arrayHist=histogram_1(imgIndexList[i])
#         #arrayHist=surfFeatures(imgIndexList[i])
#         #arrayHist=siftFeature(imgIndexList[i])
#         #arrayHist=cornerHarrris(imgIndexList[i])
#         arrayHist=starbrief(imgIndexList[i])
#         features.append(arrayHist)
#     return features
#
#
# imgIndexList=loadImg('E:\\picture\\ml\\vacation-image-search-engine\\ss')
# # # # # h1=histogram_1(imgNameList[0],imgIndexList[0])
# # # # # h2=histogram_0(imgNameList[0],imgIndexList[0])
# # # # # sf=siftFeature(imgNameList[0],imgIndexList[0])
# features=getFeature(imgIndexList)
#
# print features
# # # ###########KMeans##########
# from sklearn.cluster import KMeans
# model=KMeans(n_clusters=10)
# model.fit(features)
# labels=model.labels_
#
# #######cross_validation#####
# from sklearn import cross_validation
# train_features,test_features,train_labels,test_labels=cross_validation.train_test_split\
#  (features,labels,train_size=0.6,random_state=0)
#
# ###########SVM##########
# from sklearn import svm
# model=svm.SVC(kernel='linear')
# model.fit(train_features,train_labels)
# predict_labels=model.predict(test_features)
# count=0
# m=len(predict_labels)
# for i in range(m):
#     if predict_labels[i]==test_labels[i]:
#         count+=1
# accurancy=count*1.0/m
# print accurancy
