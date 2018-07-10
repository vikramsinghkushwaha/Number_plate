import cv2
import numpy as np
#import pytesseract

pic = cv2.imread('sample/Jeep.jpg')
img = cv2.imread('sample/Jeep.jpg')

edges = cv2.Canny(img,200,200)

contours, heirarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = int(cv2.contourArea(cnt))
    if(area > 1999 and area < 50000):
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)
        crop = img[y:y+h,x:x+w]

crop_grey = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)

cv2.imshow('edges',edges)
#cv2.imwrite('test_data/6.jpg',crop_grey)  Comment this out whe you want to write new data to file
cv2.imshow('img',img)
cv2.imshow('pic',pic)
cv2.imshow('crop_grey',crop_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()
