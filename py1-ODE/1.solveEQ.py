#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 01:05:52 2018

@author: xwen
"""

import pkuode
from random import randint
import numpy as np
import matplotlib.pyplot as plt

class EQ2(pkuode.ODE):
    def tend(self,state):
        x,y = state
        xt = 1-x**2
        yt = 1-x*y
        tendency = np.array([xt,yt])
        return tendency

if __name__=='__main__':
    a = EQ2(ic=[-0.9,-0.8],dt=0.1,steps=100)
    a.Integrate()
    a.Print()
    pkuode.plot2d(a.line,xlim=[-5,5],ylim=[-5,5])
    
    
    plt.plot(a.line[:,0],a.line[:,1],'r-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('EQ2')
    plt.xlim(-5,5)
    plt.ylim(-5,5)

    for i in range(1000):
        x0 = randint(-500,500)/100
        y0 = randint(-500,500)/100
        a = EQ2(ic=[x0,y0],dt=0.1,steps=100)
        a.Integrate()
        plt.plot(a.line[:,0],a.line[:,1],'r-',lw=0.5)
    
    plt.savefig('plotEQ2.pdf')
    plt.show()
    plt.close()
