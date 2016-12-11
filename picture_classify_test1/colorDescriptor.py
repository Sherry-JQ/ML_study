'''
Created by Sherry on 2016.10.15
The help from http://python.jobbole.com/80860/
'''
import numpy as np
import cv2

class colorDesciptor:
    def __init__(self,bins):
        self.bins=bins

    def describe(self,img):
        #change BGR to HSV
        img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        features=[]

        #get the center
        (h,w)=img.shape[:2]
        (cX,cY)=(int(w*0.5),int(h*0.5))

        #five parts--4-(top-left,top-right, bottom-right, bottom-left)
        segments=[(0,cX,0,cY),(cX,w,0,cY),(cX,w,cY,h),(0,cX,cY,h)]

        #an elliptical mask
        (axesX,axesY)=(int(w*0.75)/2,int(h*0.75)/2)
        ellipMask=np.zeros(img.shape[:2],dtype='uint8')#a empty img
        cv2.ellipse(ellipMask,(cX,cY),(axesX,axesY),0,0,360,255,-1)#still elipMask

        #four masks
        for (startX,endX,startY,endY)in segments:
            cornerMask=np.zeros(img.shape[:2],dtype='uint8')
            cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)#still cornerMask
            cornerMask=cv2.subtract(cornerMask,ellipMask)

            hist=self.histogram(img,cornerMask)
            features.append(hist)

        hist=self.histogram(img,ellipMask)
        features.append(hist)
        return features

    def histogram(self,img,mask):
        hist=cv2.calcHist([img],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
        hist=cv2.normalize(hist).flatten()
        return hist
cd=colorDesciptor((8,12,3))
img=cv2.imread('1.jpg')
img_features=cd.describe(img)
print img_features