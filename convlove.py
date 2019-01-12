# -*- coding: utf-8 -*-

"""
Created on Sat Jan 12 15:38:08 2019

@author: Muhammad Zakriya 
"""

import numpy as np
class convolve:
    def get_kernel(name,size=3,weight=2,deviation=0.84089642):
        guassian = np.zeros((size,size),dtype=np.float64)
        for x in range(size):
            for y in range(size):
                e = np.exp(-(((x+1)**2)+((y+1)**2))/(2*deviation*deviation))
                c = 1/(2*np.pi*deviation*deviation)
                guassian[x,y] = c*e
            mean = (1/(size*size))*np.ones((size,size),dtype=np.float64)
            masks = {'prewitt_x':np.array([[1,0,-1],[1,0,-1],[1,0,-1]]),
                     'prewitt_y':np.array([[1,1,1],[0,0,0],[-1,-1,-1]]),
                     'sobel_x':np.array([[-1,0,1],[-weight,0,weight],[-1,0,1]]),
                     'sobel_y':np.array([[-1,-weight,-1],[0,0,0],[1,weight,1]]),
                     'Robinson_north':np.array([[-1,0,1],[-2,0,2],[-1,0,1]]),
                     'Robinson_north_west':np.array([[0,1,2],[-1,0,1],[-2,-1,0]]),
                     'Robinson_west':np.array([[1,2,1],[0,0,0],[-1,-2,-1]]),
                     'Robinson_south_west':np.array([[2,1,0],[1,0,-1],[0,-1,-2]]),
                     'Robinson_south':np.array([[1,0,-1],[2,0,-2],[1,0,-1]]),
                     'Robinson_south_east':np.array([[0,-1,-2],[1,0,-1],[2,1,0]]),
                     'Robinson_east':np.array([[-1,-2,-1],[0,0,0],[1,2,1]]),
                     'Robinson_north_east':np.array([[-2,-1,0],[-1,0,1],[0,1,2]]),
                     'krish_north':np.array([[-3,-3,5],[-3,0,5],[-3,-3,-5]]),
                     'krish_north_west':np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]]),
                     'krish_west':np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]]),
                     'krish_south_west':np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]]),
                     'krish_south':np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]]),
                     'krish_south_east':np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]]),
                     'krish_east':np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]]),
                     'krish_north_east':np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]]),
                     'Laplacian_+':np.array([[0,1,0],[1,-4,1],[0,1,0]]),
                     'Laplacian_-':np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]),
                     'Guassian':guassian,
                     'Mean':mean
                     }
            kernel = masks[name]
            return kernel
    def conv(img,kernel):
        m,n=img.shape
        p,q=kernel.shape
        if p!=q:
            print("no of rows and column of kernel/mask should equal")
            return
        out=np.zeros((m,n))
        img = convolve.padd(img,kernel)
        for a in range(m):
            for b in range(n):
                for c in range(p):
                    for d in range(q):
                        out[a,b] = out[a,b]+(kernel[c,d]*img[a+c,b+d])
        return out
    def padd(img,kernel):
        r,c = img.shape
        kr,kc = kernel.shape
        padded = np.zeros((r+kr,c+kc),dtype=img.dtype)
        insert = np.uint((kr)/2)
        padded[insert:insert+r,insert:insert+c] = img
        return padded
