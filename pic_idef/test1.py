# encoding: utf-8
import cv2
import numpy as np
import os
from PIL import *


# import Image
# import cv2
# import numpy as np
# #hog=cv2.HOGDescriptor()
# img_pre=cv2.LoadImage('2a85.png')
# #img1=Image.open('2a85.png')
# #print img1
# print cv2.GetCol(img_pre,0)
#
# # from sklearn.feature_extraction import DictVectorizer
# # dv=DictVectorizer()
# # instances=[{'city':'New York'},{'city':'San Francisco'},{'city':'Chapel Hill'}]
# # result=dv.fit_transform(instances).toarray()
# # print result

# img=cv2.imread('E:\\picture\\third.png')
# cv2.namedWindow("Image")
# cv2.imshow("Image",img)
# cv2.waitKey(0)
#
# emptyImg=np.zeros(img.shape,np.uint8)
# emptyImg2=img.copy()
# emptyImg3=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# emptyImg3[...]=0
# cv2.imwrite("./third1.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
# cv2.imwrite("./third2.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])
#
# #cv2.imshow("Image",emptyImg)
# #cv2.imshow("Image",emptyImg2)
# cv2.imshow("Image",emptyImg3)

# def search_maxcolor(img):
#     m=img.shape[0]
#     n=img.shape[1]
#     img_array=np.zeros((1,m*n))
#     for i in range(m):
#         for j in range(n):
#             img_array[0,i*m+j]=img[i,j][0]
#     color=returnMaxColor(img_array)
#     for i in range(m):
#         for j in range(n):
#             if img[i,j][0]==color:
#                img
#
#     cv2.namedWindow("Image")
#     cv2.imshow("Image",img)
#
# def returnMaxColor(img_array):
#     b={}
#     for item in img_array[0]:
#         if item not in b:
#             b[item]=1
#         else:
#             b[item]+=1
#         return int(max(b.iteritems(), key = lambda x: x[1])[0])
# myimg = cv2.imread('2a85.png')
# search_maxcolor(myimg)
# def search_maxcolor(imgname):
#     img=cv2.imread(imgname)
#     m,n=img.size
#     for x in range(m):
#         for y in range(n):
#             pos=(x,y)
#             rgb=img.getpixel(pos)
#             (r,g,b)=rgb
#
# search_maxcolor("2a85.png")

from matplotlib import pyplot as plt
img=cv2.imread('72.jpg')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(GrayImage,160,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()