# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:02:12 2023

@author: DELL
"""

import cv2

#take path
path = input("enter path of img: ")
print(path)
#read img and convert to gray scale by passing 0 as 2nd parameter
img = cv2.imread(path,0)
print(img)

#flip if needed
img = cv2.flip(img,-1)#three params 0 , 1 ,-1

#show converted img
cv2.imshow("Gray scale image",img)



#now store /save converted img
k = cv2.waitKey(0)

#when click ctrl+s
if k == ord("s"):
    cv2.imwrite("D:\Sem 5\CV\code\img222.jpg",img)
else:
    cv2.destroyAllWindowa()