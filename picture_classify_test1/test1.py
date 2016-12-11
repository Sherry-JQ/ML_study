#encoding=utf-8
'''
A test for base picture classify.
Use SVM、cluster and classify knowledges.
Help from http://blog.csdn.net/always2015/article/details/47100713
Created by Sherry on 2016.10.11
'''

# for picture features
#import cv2
# from numpy import *
# from os import listdir
# def getPicFeatures_1(direction):
#     dataFileNameList=listdir(direction)
#     m=len(dataFileNameList)
#     for i in range(m):
#         #读取图片
#         picname=dataFileNameList[i]
#         img_0=cv2.imread(picname)
#         #下采样
#         img_lowers=cv2.pyrDown(img_0)
#         #灰度
#         img_gray=cv2.cvtColor(img_lowers,cv2.COLOR_RGB2GRAY)
#         #检测特征点
#        s=cv2.SURF()
#         mask=uint8(ones(img_gray.shape))
#         keypoints=s.detect(img_gray,mask)
#
# img_0=cv2.imread('E://picture//first.jpg',0)
#下采样
#img_lowers=cv2.pyrDown(img_0)
#灰度
#img_gray=cv2.cvtColor(img_lowers,cv2.COLOR_RGB2GRAY)
#检测特征点
#s=cv2.SURF(400)
# kp,des=s.detectAndCompute(img_0,None)
# print len(kp)

# import cv2
# import numpy as np
#
# img = cv2.imread('1.jpg')
#
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# # surf.hessianThreshold=3000
# surf = cv2.SURF(3000)
#
# kp,res = surf.detectAndCompute(gray,None)
# print res.shape
#
# img = cv2.drawKeypoints(img,kp,None,(255,0,255),4)
# print(len(kp))
#
# cv2.namedWindow("SURF")
# cv2.imshow("SURF", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# #deskew图片抗扭曲
# def deskew(img):
#     m=cv2.imread(img,0)
#     rows,cols=m.shape
#     # if abs(m['mu02'])<1e-2:
#     #     return img.copy()
#     # skew=m['mu11']/m['mu02']
#     M=np.float32([[1,0,100],[0,1,50]])
#     dstimg=cv2.warpAffine(m,M,(cols,rows))
#     cv2.imshow('changed_img',dstimg)
#     cv2.waitKey(0)
# deskew('1.jpg')
#
import cv2
import numpy as np
#
# img = cv2.imread('1.jpg',0)
# rows,cols = img.shape
#
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))
#
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# SZ=20
# affine_flags=cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR
# def deskew(img):
#     m = cv2.moments(img)
#     if abs(m['mu02']) < 1e-2:
#         return img.copy()
#     skew = m['mu11']/m['mu02']
#     M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
#     img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
#     return img
# deskew('1.jpg')


# #特征提取__SIFT
# import cv2
# im=cv2.imread('E:\\picture\\SVM_pic\\airplane\\airp_1.jpg')
# s=cv2.SIFT()
# keypoints = s.detect(im)
# kp,des=s.detectAndCompute(im,None)
# # # 显示特征点
# # print len(kp)
# # for k in keypoints:
# #     cv2.circle(im,(int(k.pt[0]),int(k.pt[1])),1,(0,255,0),-1)
# #     #cv2.circle(im,(int(k.pt[0]),int(k.pt[1])),int(k.size),(0,255,0),2)
# #
# # cv2.imshow('SURF_features',im)
# # cv2.waitKey()
# # cv2.destroyAllWindows()
# # from sklearn.cluster import KMeans
# # print kp

#特征提取__直方图
import cv2
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread('E:\\picture\\SVM_pic\\airplane\\airp_1.jpg')
img2=cv2.imread('E:\\picture\\SVM_pic\\airplane\\airp_2.jpg')
ch1=cv2.calcHist(img1,[0],None,[256],[0.0,255.0])
ch2=cv2.calcHist(img2,[0],None,[256],[0.0,255.0])
print ch1,ch1.size
plt.plot(range(256),ch1,'r')
plt.plot(range(256),ch2,'b')
hist1=ch1
hist2=ch2
plt.show()
degree = 0
for i in range(len(hist1)):
    if hist1[i] != hist2[i]:
        degree = degree + (1 - abs(hist1[i]-hist2[i])/max(hist1[i],hist2[i]))
    else:
        degree = degree + 1
degree = degree/len(hist1)
print degree
fea_det = cv2.FeatureDetector_create("SIFT")
des_ext = cv2.DescriptorExtractor_create("SIFT")