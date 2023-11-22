import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('C://Users//Hp//Desktop//LeatherDefectDetection//hello.jpg')
img = cv2.resize(img1, (960, 540)) 

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(imgray, 127, 255, 0)

ret,thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours = " + str(len(contours)) )


edged = cv2.Canny(imgray, 30, 200)
cv2.waitKey(0)



areas = []
for c in contours:
    areas.append(cv2.contourArea(c))
print(areas)
    
    
    
max=max(areas[0],areas[1]) 
secondmax=min(areas[0],areas[1]) 
  
for i in range(2,len(areas)): 
    if areas[i]>max: 
        secondmax=max
        max=areas[i] 
    else: 
        if areas[i]>secondmax: 
            secondmax=areas[i]
            int(secondmax)
  
print("Second highest number is : ",str(secondmax)) 
index = areas.index(secondmax)
print(index)
#print(type(secondmax))


cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

#print (contours)

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgray)
cv2.imshow('CannyEdged', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()