# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:41:56 2019

@author: zakriya
"""

import cv2
import convolve
import numpy as np
img = cv2.imread('cameraman.tif',0)
img = img/255
img_color = cv2.imread('football.jpg',1)
img_color = img_color/255
masks = ['prewitt_x',
         'prewitt_y',
         'sobel_x',
         'sobel_y',
         'Robinson_north',
         'Robinson_north_west',
         'Robinson_west',
         'Robinson_south_west',
         'Robinson_south',
         'Robinson_south_east',
         'Robinson_east',
         'Robinson_north_east',
         'krish_north',
         'krish_north_west',
         'krish_west',
         'krish_south_west',
         'krish_south',
         'krish_south_east',
         'krish_east',
         'krish_north_east',
         'Laplacian_+',
         'Laplacian_-',
         'Guassian',
         'Mean']
                     


for name in masks:
    kernel = convolve.convolve.get_kernel(name)
    out = convolve.convolve.conv(img,kernel)
    cv2.imshow(name,out)
    #cv2.imwrite('%s.png'%name,out)
cv2.waitKey(0)
cv2.destroyAllWindows()

for name in masks:
    kernel = convolve.convolve.get_kernel(name)
    out0 = convolve.convolve.conv(img_color[:,:,0],kernel)
    out1  = convolve.convolve.conv(img_color[:,:,1],kernel)
    out2 = convolve.convolve.conv(img_color[:,:,2],kernel)
    result = cv2.merge((out0,out1,out2))
    cv2.imshow(name,result)
    #cv2.imwrite('%s_color.png'%name,out)
cv2.waitKey(0)
cv2.destroyAllWindows()
