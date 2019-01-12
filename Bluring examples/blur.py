# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:57:45 2019

@author: zakriya
"""
import cv2
import convolve as cn

#read image from disk
img = cv2.imread('football.png',1)
#convert image values in between 0 to 1
img = img/255
#split image in 3
img_r = img[:,:,0]
img_g = img[:,:,1]
img_b = img[:,:,2]

#find the edges of each color using a same filter
kernel = cn.convolve.get_kernel('Mean',size=3)
out_r = cn.convolve.conv(img_r,kernel)
out_g = cn.convolve.conv(img_g,kernel)
out_b = cn.convolve.conv(img_b,kernel)

#now merge them in one
out = cv2.merge((out_r,out_g,out_b))


#see the result

cv2.imshow('Mean_blur',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
