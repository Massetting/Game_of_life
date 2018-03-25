#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 00:05:52 2018

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt

#maze=np.random.randint(0,2,size=(100,100))
x_size=100
y_size=100
maze=np.zeros((y_size,x_size))
#x_pos=np.random.choice(np.arange(0,99))
#y_pos=np.random.choice(np.arange(0,99))
#seed=(y_pos,x_pos)
#maze[seed]=1
def gosper_glider_gun(maze)
#gosper glider gun
#square
    maze[5,1]=1
    maze[6,1]=1
    maze[5,2]=1
    maze[6,2]=1
    #middle
    maze[4,11]=1
    maze[5,11]=1
    maze[6,11]=1
    maze[7,12]=1
    maze[3,12]=1
    maze[8,13]=1
    maze[8,14]=1
    maze[2,13]=1
    maze[2,14]=1
    maze[5,15]=1
    maze[7,16]=1
    maze[3,16]=1
    maze[4,17]=1
    maze[5,17]=1
    maze[6,17]=1
    maze[5,18]=1
    #successive
    maze[6,21]=1
    maze[7,21]=1
    maze[8,21]=1
    maze[6,22]=1
    maze[7,22]=1
    maze[8,22]=1
    maze[9,23]=1
    maze[5,23]=1
    maze[9,25]=1
    maze[10,25]=1
    maze[5,25]=1
    maze[4,25]=1
    #final square
    maze[7,35]=1
    maze[8,35]=1
    maze[7,36]=1
    maze[8,36]=1
    return maze




plt.ion()
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.imshow(maze)
plt.pause(0.1) 
#a=[]

for i in range(10000):
#    input("press")
    for x in range(x_size):
        for y in range(y_size):
            bc=(y-1,x)
            bl=(y-1,x-1)
            ml=(y,x-1)
            ul=(y+1,x-1)
            uc=(y+1,x)
            ur=(y+1,x+1)
            mr=(y,x+1)
            br=(y-1,x+1)
            
            if x+1>x_size-1 and y+1>y_size-1:
                neighbors=maze[bc]+maze[bl]+maze[ml]
            elif x+1>x_size-1:
                 neighbors=maze[bc]+maze[bl]+maze[ml]+maze[ul]+maze[uc]
            elif y+1>y_size-1:
                 neighbors=maze[bc]+maze[bl]+maze[ml]+maze[mr]+maze[br]
            
            elif x-1<0:
                 neighbors=maze[bc]+maze[uc]+maze[ur]+maze[mr]+maze[br]                
            elif y-1<0:
                 neighbors=maze[ml]+maze[ul]+maze[uc]+maze[ur]+maze[mr]

            else:#if x+1<x_size and y+1<y_size and :
                neighbors=maze[bc]+maze[bl]+maze[ml]+maze[ul]+maze[uc]+maze[ur]+maze[mr]+maze[br]
            if maze[y,x]==1:
                if neighbors<2:
                    maze[y,x]=0
                if neighbors<=3:
                    maze[y,x]=1
                if neighbors>3:
                    maze[y,x]=0
            if maze[y,x]==0:
                if neighbors==3:
                    maze[y,x]=1
    #time.sleep(3)
#    input("press")
    plt.cla()
    plt.text(0,0,"generation:  {}".format(i))    
    ax.imshow(maze)
    plt.pause(0.01) 

#    plt.show()
        
