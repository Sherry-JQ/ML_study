import cv2
image=cv2.imread("face7.jpg")
facecascade=cv2.CascadeClassifier("D:\OpenCV\OpenCV-install\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
#gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray=cv2.imread("face7.jpg",0)
#detect setting
faces=facecascade.detectMultiScale(gray,1.2,5)

for (x,y,w,h)in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces found",image)
cv2.waitKey(0)
